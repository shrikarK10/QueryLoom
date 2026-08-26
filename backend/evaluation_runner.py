import sys
import json
import time
import traceback
from pathlib import Path
import sqlite3

# Set up paths
backend_dir = Path(__file__).resolve().parent
sys.path.append(str(backend_dir))

from connectors.sqlite_connector import SQLiteConnector
from pipeline.querymind_pipeline import run_querymind
from utils.config import DB_PATH
from utils.logger import set_silent_mode

def normalize_value(val):
    if val is None:
        return None
    if isinstance(val, float):
        return round(val, 2)
    if isinstance(val, (bytes, bytearray)):
        return val.decode("utf-8", errors="replace")
    return val

def normalize_row(row):
    return tuple(normalize_value(x) for x in row)

def compare_results(expected, actual, is_ordered=False):
    if expected is None or actual is None:
        return False
        
    if len(expected) != len(actual):
        return False
        
    norm_expected = [normalize_row(r) for r in expected]
    norm_actual = [normalize_row(r) for r in actual]
    
    if not is_ordered:
        try:
            norm_expected.sort(key=lambda x: str(x))
            norm_actual.sort(key=lambda x: str(x))
        except Exception:
            # Fallback if sorting fails
            pass
            
    return norm_expected == norm_actual

def check_partial_match(expected_data, actual_data):
    if not expected_data or not actual_data:
        return False
    if len(expected_data) != len(actual_data):
        return False
        
    norm_expected = [normalize_row(r) for r in expected_data]
    norm_actual = [normalize_row(r) for r in actual_data]
    
    # Check if first column matches (e.g. key entity names)
    first_col_exp = set(r[0] for r in norm_expected if len(r) > 0)
    first_col_act = set(r[0] for r in norm_actual if len(r) > 0)
    
    if first_col_exp == first_col_act and len(first_col_exp) > 0:
        return True
        
    # Check if any column in actual matches the first column of expected
    for col_idx in range(len(norm_actual[0]) if norm_actual else 0):
        col_act = set(r[col_idx] for r in norm_actual if len(r) > col_idx)
        if first_col_exp == col_act:
            return True
            
    return False

def classify_failure(r, partial_matched=False):
    reason = r.get("failure_reason") or ""
    gen_sql = (r.get("generated_sql") or "").lower()
    expected_sql = (r.get("expected_sql") or "").lower()
    
    if "Pipeline crashed" in reason:
        return "Execution"
    if "ambiguous column" in reason.lower() or "no such column" in reason.lower() or "no such table" in reason.lower():
        return "Execution"
        
    # Check if ordering is mismatched
    is_ordered_expected = "order by" in expected_sql
    is_ordered_actual = "order by" in gen_sql
    if is_ordered_expected and not is_ordered_actual:
        return "Planner"
        
    # Check if aggregate function differs
    agg_funcs = ["count(", "sum(", "avg(", "min(", "max("]
    any_agg_expected = any(f in expected_sql for f in agg_funcs)
    any_agg_actual = any(f in gen_sql for f in agg_funcs)
    if any_agg_expected != any_agg_actual:
        return "Aggregation"
    for f in agg_funcs:
        if (f in expected_sql) != (f in gen_sql):
            return "Aggregation"
            
    # Check if conditions differ (WHERE clause exists/mismatched)
    if ("where" in expected_sql) != ("where" in gen_sql):
        return "Condition"
        
    # Check if join count differs heavily
    join_count_expected = expected_sql.count("join")
    join_count_actual = gen_sql.count("join")
    if abs(join_count_expected - join_count_actual) > 0:
        return "Join"
        
    if partial_matched:
        return "Projection"
        
    if "Row count mismatch" in reason:
        if r.get("actual_rows", 0) == 0:
            return "Condition"
        return "Join"
        
    return "Prompt"

def main():
    set_silent_mode(True)
    connector = SQLiteConnector(DB_PATH)
    
    # Load dataset dynamically based on active DB
    if "Chinook" in DB_PATH:
        dataset_name = "evaluation_dataset_chinook.json"
        report_path = backend_dir / "evaluation_report_chinook.md"
    else:
        dataset_name = "evaluation_dataset.json"
        report_path = backend_dir / "evaluation_report_V2.5(New_planner_changes).md"
        
    dataset_path = backend_dir / dataset_name
    with open(dataset_path, "r", encoding="utf-8") as f:
        test_cases = json.load(f)
        
    print(f"Loaded {len(test_cases)} test cases from {dataset_path.name}")
    
    results = []
    total_latency = 0.0
    
    for idx, tc in enumerate(test_cases, 1):
        q_id = tc["id"]
        question = tc["question"]
        expected_sql = tc["expected_sql"]
        difficulty = tc["difficulty"]
        
        pct = int((idx / len(test_cases)) * 100)
        filled = int(20 * idx // len(test_cases))
        bar = '=' * filled + '-' * (20 - filled)
        print(f"\nProgress: [{bar}] {pct}% | Query {idx}/{len(test_cases)} (ID: {q_id}, {difficulty})")

        print(f"Question: {question}")
        
        # 1. Get ground truth
        try:
            expected_data = connector.execute_query(expected_sql)
            expected_error = None
        except Exception as e:
            expected_data = []
            expected_error = f"Expected SQL execution failed: {e}"
            print(f"  !! Ground truth query failed to run: {e}")
            
        # 2. Run QueryMind pipeline
        start_time = time.time()
        pipeline_error = None
        gen_sql = None
        actual_data = []
        
        try:
            pipeline_result = run_querymind(question, connector)
            gen_sql = pipeline_result.get("sql")
            actual_data = pipeline_result.get("result", [])
            if "error" in pipeline_result and not gen_sql:
                pipeline_error = pipeline_result["error"]
        except Exception as e:
            pipeline_error = f"Pipeline crashed: {e}\n{traceback.format_exc()}"
            print(f"  !! Pipeline crashed: {e}")
            
        latency = time.time() - start_time
        total_latency += latency
        
        # 3. Compare results
        is_ordered = "order by" in expected_sql.lower()
        
        passed_strict = False
        passed_partial = False
        failure_reason = None
        
        if expected_error:
            failure_reason = expected_error
        elif pipeline_error:
            failure_reason = f"QueryMind failed: {pipeline_error}"
        else:
            passed_strict = compare_results(expected_data, actual_data, is_ordered=is_ordered)
            if not passed_strict:
                passed_partial = check_partial_match(expected_data, actual_data)
                if len(expected_data) != len(actual_data):
                    failure_reason = f"Row count mismatch (Expected: {len(expected_data)}, Actual: {len(actual_data)})"
                else:
                    failure_reason = "Data content mismatch"
                    
        failure_cat = None
        if not passed_strict:
            failure_cat = classify_failure({
                "question": question,
                "expected_sql": expected_sql,
                "generated_sql": gen_sql,
                "expected_rows": len(expected_data),
                "actual_rows": len(actual_data),
                "failure_reason": failure_reason
            }, partial_matched=passed_partial)
            
        results.append({
            "id": q_id,
            "question": question,
            "difficulty": difficulty,
            "expected_sql": expected_sql,
            "generated_sql": gen_sql,
            "expected_rows": len(expected_data),
            "actual_rows": len(actual_data),
            "passed_strict": passed_strict,
            "passed_partial": passed_partial,
            "latency_seconds": latency,
            "failure_reason": failure_reason,
            "failure_category": failure_cat
        })
        
        if passed_strict:
            status_str = "PASS (Strict)"
        elif passed_partial:
            status_str = f"PARTIAL PASS (tagged: {failure_cat})"
        else:
            status_str = f"FAIL (reason: {failure_reason}, tagged: {failure_cat})"
            
        print(f"  -> {status_str} (took {latency:.2f}s)")
        
    # Calculate statistics
    total = len(results)
    strict_count = sum(1 for r in results if r["passed_strict"])
    partial_count = sum(1 for r in results if r["passed_partial"])
    failed_count = total - strict_count - partial_count
    
    strict_rate = (strict_count / total) * 100 if total > 0 else 0
    semantic_rate = ((strict_count + partial_count) / total) * 100 if total > 0 else 0
    avg_latency = total_latency / total if total > 0 else 0
    
    diff_stats = {}
    for r in results:
        diff = r["difficulty"]
        if diff not in diff_stats:
            diff_stats[diff] = {"total": 0, "passed_strict": 0, "passed_partial": 0}
        diff_stats[diff]["total"] += 1
        if r["passed_strict"]:
            diff_stats[diff]["passed_strict"] += 1
        elif r["passed_partial"]:
            diff_stats[diff]["passed_partial"] += 1
            
    print("\n" + "="*40)
    print("EVALUATION COMPLETED")
    print(f"Total Queries: {total}")
    print(f"Strict Passed: {strict_count}")
    print(f"Partial Passed: {partial_count}")
    print(f"Failed: {failed_count}")
    print(f"Strict Accuracy: {strict_rate:.2f}%")
    print(f"Semantic/Partial Match Accuracy: {semantic_rate:.2f}%")
    print(f"Avg Latency: {avg_latency:.2f}s")
    print("="*40)
    
    # Write report
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# QueryMind Evaluation Report\n\n")
        f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Performance Summary\n\n")
        f.write("| Metric | Value |\n")
        f.write("| --- | --- |\n")
        f.write(f"| **Total Queries** | {total} |\n")
        f.write(f"| **Strict Passed** | {strict_count} |\n")
        f.write(f"| **Partial Passed** | {partial_count} |\n")
        f.write(f"| **Failed** | {failed_count} |\n")
        f.write(f"| **Strict Accuracy** | **{strict_rate:.2f}%** |\n")
        f.write(f"| **Semantic / Partial Match Accuracy** | **{semantic_rate:.2f}%** |\n")
        f.write(f"| **Average Latency** | {avg_latency:.2f}s |\n\n")
        
        f.write("## Difficulty Breakdown\n\n")
        f.write("| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |\n")
        f.write("| --- | --- | --- | --- | --- |\n")
        for diff, stats in diff_stats.items():
            diff_rate = ((stats["passed_strict"] + stats["passed_partial"]) / stats["total"]) * 100
            f.write(f"| {diff.capitalize()} | {stats['total']} | {stats['passed_strict']} | {stats['passed_partial']} | {diff_rate:.2f}% |\n")
        f.write("\n")
        
        f.write("## Failure Analysis Details\n\n")
        
        # Unpassed results (includes partial matches and total failures)
        unpassed_results = [r for r in results if not r["passed_strict"]]
        if not unpassed_results:
            f.write("🎉 **All queries strictly passed!**\n")
        else:
            # Let's count failure category occurrences
            cat_counts = {}
            for r in unpassed_results:
                cat = r["failure_category"]
                cat_counts[cat] = cat_counts.get(cat, 0) + 1
                
            f.write("### Failure / Projection Categorization Breakdown\n\n")
            f.write("| Category | Count |\n")
            f.write("| --- | --- |\n")
            for cat, count in cat_counts.items():
                f.write(f"| **{cat}** | {count} |\n")
            f.write("\n---\n\n")
            
            for r in unpassed_results:
                status_label = "PARTIAL PASS" if r["passed_partial"] else "FAIL"
                f.write(f"### Test ID {r['id']} ({r['difficulty'].capitalize()}) - [{status_label}]\n")
                f.write(f"**Question:** `{r['question']}`\n\n")
                f.write(f"**Failure Category:** **{r['failure_category']}**\n\n")
                f.write(f"**Failure Reason:** *{r['failure_reason']}*\n\n")
                f.write("**Expected SQL:**\n")
                f.write(f"```sql\n{r['expected_sql']}\n```\n\n")
                f.write("**Generated SQL:**\n")
                f.write(f"```sql\n{r['generated_sql'] or 'None'}\n```\n\n")
                f.write(f"**Expected Row Count:** {r['expected_rows']} | **Actual Row Count:** {r['actual_rows']}\n")
                f.write("\n---\n\n")
                
    print(f"Report written to {report_path}")

if __name__ == "__main__":
    main()
