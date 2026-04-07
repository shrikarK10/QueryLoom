from llm.sql_reflector import reflect_sql
from llm.sql_generator import generate_sql
from llm.llm_planner import plan_query
from utils.logger import logger as log, file_logger
from utils.sql_validator import validate_sql
from utils.schema_updater import format_schema, build_column_mapping
from utils.relationship_extractor import (
    extract_relationships,
    build_relationship_graph,
    find_join_path,
    build_joins
)
from utils.column_mapper import build_column_to_table_map

import re
import json


def _classify_query_type(query: str) -> str:
    q = query.lower()

    if any(token in q for token in [
        "each", "per", "group by", "rank", "compare", "running", "cumulative",
        "difference", "percentile", "ratio", "proportion", "distribution", "trend",
        "month over month", "year over year", "yoy", "mom"
    ]):
        return "ANALYTICAL"

    if any(token in q for token in [
        "how many", "count", "total", "sum", "average", "avg", "mean", "min", "max",
        "overall", "altogether"
    ]):
        return "AGGREGATION"

    if any(token in q for token in [
        "top", "highest", "lowest", "first", "last", "list", "show", "find",
        "display", "get", "who", "what", "which", "give me", "return"
    ]):
        return "SIMPLE_SELECT"

    return "GENERAL"


def _extract_limit_from_query(query: str) -> int | None:
    match = re.search(r"\b(?:top|first)\s+(\d+)\b", query.lower())
    if match:
        return int(match.group(1))
    return None


def _enforce_simple_limit(sql: str, query: str, query_type: str) -> str:
    if query_type != "SIMPLE_SELECT":
        return sql

    lower_sql = sql.lower()
    if "limit" in lower_sql:
        return sql
    if any(token in lower_sql for token in ["count(", "sum(", "avg(", "group by"]):
        return sql

    requested_limit = _extract_limit_from_query(query)
    if requested_limit is None and any(token in query.lower() for token in ["list", "show"]):
        requested_limit = 20
    if requested_limit is None:
        return sql

    return sql.rstrip().rstrip(";") + f"\nLIMIT {requested_limit};"


# ---------------------------
# NEW HELPERS
# ---------------------------
def pick_best_table(col, table_list, schema, graph, query):
    for t in table_list:
        if t.lower() in query.lower():
            return t

    table_list = sorted(table_list, key=lambda t: len(schema[t]))
    table_list = sorted(table_list, key=lambda t: -len(graph.get(t, [])))

    return table_list[0]

def extract_columns_from_condition(condition: str):
    if condition == "NONE":
        return []

    tokens = re.findall(r"[A-Za-z_]+", condition)

    return [
        t for t in tokens
        if t in condition and t[0].isupper() and t.lower() not in ["and", "or"]
    ]

def get_tables_from_columns(columns, column_to_table, schema, graph, query):
    tables = set()

    for col in columns:
        # handle functions like SUM(TotalDue)
        if "(" in col:
            col = col.split("(")[-1].replace(")", "")

        if col in column_to_table:
            possible_tables = column_to_table[col]

            best_table = pick_best_table(col, possible_tables, schema, graph, query)
            tables.add(best_table)

    return list(tables)


# ---------------------------
# MAIN PIPELINE
# ---------------------------

def run_querymind(query: str, connector):
    file_logger("Start", "")
    log("User Query", query)
    file_logger("User Query", query)

    # Query Type
    query_type = _classify_query_type(query)
    log("Query Type", query_type)
    file_logger("Query Type", query_type)

    # Schema
    schema = connector.get_schema()

    # Relationships (dynamic)
    relationships = extract_relationships(connector)
    graph = build_relationship_graph(relationships)

    # Format schema
    formatted_schema = format_schema(schema)
    log("Schema Extracted", formatted_schema)

    # Column mapping (LLM use only)
    column_mapping = build_column_mapping(schema)
    log("Column Mapping", column_mapping)

    # ---------------------------
    # PLANNER
    # ---------------------------
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
    query_plan = json.loads(query_plan_raw)

    log("Query Plan", query_plan)
    file_logger("Query Plan", query_plan)

    # ---------------------------
    # COLUMN → TABLE RESOLUTION (NEW CORE)
    # ---------------------------
    column_to_table = build_column_to_table_map(schema)
    file_logger("Column to Table Map", column_to_table)
    
    columns = query_plan["columns_needed"]
    file_logger("Columns Needed", columns)
    
    condition_cols = extract_columns_from_condition(query_plan["conditions"])
    file_logger("Condition Columns", condition_cols)
    
    all_columns = list(set(columns + condition_cols))
    file_logger("All Columns", all_columns)
    
    tables = get_tables_from_columns(all_columns, column_to_table, schema, graph, query)

    log("Resolved Tables", tables)
    file_logger("Resolved Tables", tables)

    # ---------------------------
    # JOIN GENERATION (NEW CORE)
    # ---------------------------
    if len(tables) > 1:
        full_path = []

        for i in range(len(tables) - 1):
            path = find_join_path(graph, tables[i], tables[i + 1])

            if path:
                if not full_path:
                    full_path.extend(path)
                else:
                    full_path.extend(path[1:])

        joins = build_joins(full_path, relationships)
    else:
        joins = ""

    log("Generated Joins", joins)
    file_logger("Generated Joins", joins)

    # ---------------------------
    # GENERATOR
    # ---------------------------
    sql_query = generate_sql(
        query,
        formatted_schema,
        column_mapping,
        query_plan=query_plan,
        joins=joins,
        query_type=query_type
    )

    sql_query = _enforce_simple_limit(sql_query, query, query_type)

    log("Generated SQL", sql_query)
    file_logger("Generated SQL", sql_query)

    # ---------------------------
    # REFLECTOR
    # ---------------------------
    corrected_sql = reflect_sql(
        question=query,
        schema=formatted_schema,
        sql_query=sql_query,
        column_mapping=column_mapping,
        query_plan=query_plan,
        joins=joins,
        query_type=query_type
    )

    corrected_sql = _enforce_simple_limit(corrected_sql, query, query_type)

    log("Reflected SQL", corrected_sql)
    file_logger("Reflected SQL", corrected_sql)

    # ---------------------------
    # VALIDATION
    # ---------------------------
    valid_gen, err_gen = validate_sql(connector, sql_query)
    valid_ref, err_ref = validate_sql(connector, corrected_sql)

    log("Generated SQL Valid?", valid_gen)
    log("Reflected SQL Valid?", valid_ref)

    file_logger("Generated SQL Valid?", valid_gen)
    file_logger("Reflected SQL Valid?", valid_ref)

    # ---------------------------
    # RETRY LOOP
    # ---------------------------
    if not valid_gen and not valid_ref:
        retry_error = f"Generated SQL error: {err_gen}\nReflected SQL error: {err_ref}"

        log("Retrying with feedback", retry_error)
        file_logger("Retrying with feedback", retry_error)

        sql_query = generate_sql(
            query,
            formatted_schema,
            column_mapping,
            query_plan=query_plan,
            joins=joins,
            query_type=query_type,
            previous_error=retry_error
        )

        corrected_sql = reflect_sql(
            query,
            formatted_schema,
            sql_query,
            query_plan=query_plan,
            joins=joins,
            query_type=query_type,
            previous_error=retry_error
        )

        sql_query = _enforce_simple_limit(sql_query, query, query_type)
        corrected_sql = _enforce_simple_limit(corrected_sql, query, query_type)

        valid_gen, err_gen = validate_sql(connector, sql_query)
        valid_ref, err_ref = validate_sql(connector, corrected_sql)

        log("Retry Generated SQL Valid?", valid_gen)
        log("Retry Reflected SQL Valid?", valid_ref)

        file_logger("Retry Generated SQL Valid?", valid_gen)
        file_logger("Retry Reflected SQL Valid?", valid_ref)

    # ---------------------------
    # EXECUTION
    # ---------------------------
    candidates = []

    if valid_gen:
        try:
            gen_result = connector.execute_query(sql_query)
            candidates.append(("generator", sql_query, gen_result))
        except Exception as e:
            log("Generated SQL execution failed", str(e))

    if valid_ref:
        try:
            ref_result = connector.execute_query(corrected_sql)
            candidates.append(("reflection", corrected_sql, ref_result))
        except Exception as e:
            log("Reflected SQL execution failed", str(e))

    if not candidates:
        return {
            "error": f"Both queries failed:\nGen: {err_gen}\nRef: {err_ref}",
            "sql": None,
            "result": []
        }

    best = candidates[0]

    for source, candidate_sql, candidate_result in candidates:
        if len(candidate_result) > 0 and len(best[2]) == 0:
            best = (source, candidate_sql, candidate_result)
        elif source == "reflection" and len(candidate_result) > 0:
            best = (source, candidate_sql, candidate_result)

    selected_source, final_sql, result = best

    log("Selected SQL Source", selected_source)
    log("Execution Result", result)

    file_logger("Final SQL", final_sql)
    file_logger("Selected SQL Source", selected_source)
    file_logger("Execution Result", result)

    return {
        "sql": final_sql,
        "result": result
    }