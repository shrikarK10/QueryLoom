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

def main():
    connector = SQLiteConnector(DB_PATH)
    
    # Load dataset
    dataset_path = backend_dir / "evaluation_dataset.json"
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
        
        print(f"[{idx}/{len(test_cases)}] Running ID {q_id} ({difficulty}): {question}")
        
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
        
        passed = False
        failure_reason = None
        
        if expected_error:
            failure_reason = expected_error
        elif pipeline_error:
            failure_reason = f"QueryMind failed: {pipeline_error}"
        else:
            passed = compare_results(expected_data, actual_data, is_ordered=is_ordered)
            if not passed:
                if len(expected_data) != len(actual_data):
                    failure_reason = f"Row count mismatch (Expected: {len(expected_data)}, Actual: {len(actual_data)})"
                else:
                    failure_reason = "Data content mismatch"
                    
        results.append({
            "id": q_id,
            "question": question,
            "difficulty": difficulty,
            "expected_sql": expected_sql,
            "generated_sql": gen_sql,
            "expected_rows": len(expected_data),
            "actual_rows": len(actual_data),
            "passed": passed,
            "latency_seconds": latency,
            "failure_reason": failure_reason
        })
        
        status_str = "PASS" if passed else f"FAIL ({failure_reason})"
        print(f"  -> {status_str} (took {latency:.2f}s)")
        
    # Calculate statistics
    total = len(results)
    passed_count = sum(1 for r in results if r["passed"])
    failed_count = total - passed_count
    pass_rate = (passed_count / total) * 100 if total > 0 else 0
    avg_latency = total_latency / total if total > 0 else 0
    
    diff_stats = {}
    for r in results:
        diff = r["difficulty"]
        if diff not in diff_stats:
            diff_stats[diff] = {"total": 0, "passed": 0}
        diff_stats[diff]["total"] += 1
        if r["passed"]:
            diff_stats[diff]["passed"] += 1
            
    print("\n" + "="*40)
    print("EVALUATION COMPLETED")
    print(f"Total Queries: {total}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Pass Rate: {pass_rate:.2f}%")
    print(f"Avg Latency: {avg_latency:.2f}s")
    print("="*40)
    
    # Write report
    report_path = backend_dir / "evaluation_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# QueryMind Evaluation Report\n\n")
        f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Performance Summary\n\n")
        f.write("| Metric | Value |\n")
        f.write("| --- | --- |\n")
        f.write(f"| **Total Queries** | {total} |\n")
        f.write(f"| **Passed** | {passed_count} |\n")
        f.write(f"| **Failed** | {failed_count} |\n")
        f.write(f"| **Overall Pass Rate** | **{pass_rate:.2f}%** |\n")
        f.write(f"| **Average Latency** | {avg_latency:.2f}s |\n\n")
        
        f.write("## Difficulty Breakdown\n\n")
        f.write("| Difficulty | Total | Passed | Pass Rate |\n")
        f.write("| --- | --- | --- | --- |\n")
        for diff, stats in diff_stats.items():
            diff_rate = (stats["passed"] / stats["total"]) * 100
            f.write(f"| {diff.capitalize()} | {stats['total']} | {stats['passed']} | {diff_rate:.2f}% |\n")
        f.write("\n")
        
        f.write("## Failure Analysis Details\n\n")
        f.write("Below are the details of the failed queries. Review them to identify the root cause category: **Ambiguity**, **Join**, **Planner**, or **Prompt**.\n\n")
        
        failed_results = [r for r in results if not r["passed"]]
        if not failed_results:
            f.write("🎉 **All queries passed!**\n")
        else:
            for r in failed_results:
                f.write(f"### Test ID {r['id']} ({r['difficulty'].capitalize()})\n")
                f.write(f"**Question:** `{r['question']}`\n\n")
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
