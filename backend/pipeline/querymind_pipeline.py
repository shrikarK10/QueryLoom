from llm.sql_reflector import reflect_sql
from llm.sql_generator import generate_sql
from llm.llm_planner import plan_query
from utils.logger import logger as log
from utils.sql_validator import validate_sql
from utils.schema_updater import format_schema , build_column_mapping
import re


def _classify_query_type(query: str) -> str:
    q = query.lower()
    if any(token in q for token in ["how many", "count", "total number"]):
        return "AGGREGATION"
    if any(token in q for token in ["top", "highest", "lowest", "first", "last", "list", "show"]):
        return "SIMPLE_SELECT"
    if any(token in q for token in ["each", "per", "average", "sum", "group by"]):
        return "ANALYTICAL"
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


def run_querymind(query: str, connector):
    log("User Query", query)
    query_type = _classify_query_type(query)
    log("Query Type", query_type)

    schema = connector.get_schema()

    formatted_schema = format_schema(schema)
    log("Schema Extracted", formatted_schema)

    column_mapping = build_column_mapping(schema)
    log("Column Mapping", column_mapping)

    query_plan = plan_query(query, formatted_schema, column_mapping)
    log("Query Plan", query_plan)

    sql_query = generate_sql(query, formatted_schema, column_mapping, query_plan=query_plan, query_type=query_type)
    sql_query = _enforce_simple_limit(sql_query, query, query_type)
    log("Generated SQL", sql_query)

    corrected_sql = reflect_sql(query, formatted_schema, sql_query, column_mapping, query_plan=query_plan, query_type=query_type)
    corrected_sql = _enforce_simple_limit(corrected_sql, query, query_type)
    log("Reflected SQL", corrected_sql)

    valid_gen, err_gen = validate_sql(connector, sql_query)
    valid_ref, err_ref = validate_sql(connector, corrected_sql)

    log("Generated SQL Valid?", valid_gen)
    log("Reflected SQL Valid?", valid_ref)

    if not valid_gen and not valid_ref:
        retry_error = f"Generated SQL error: {err_gen}\nReflected SQL error: {err_ref}"
        log("Retrying with feedback", retry_error)

        sql_query = generate_sql(
            query,
            formatted_schema,
            column_mapping,
            query_plan=query_plan,
            query_type=query_type,
            previous_error=retry_error
        )
        corrected_sql = reflect_sql(
            query,
            formatted_schema,
            sql_query,
            column_mapping,
            query_plan=query_plan,
            query_type=query_type,
            previous_error=retry_error
        )

        sql_query = _enforce_simple_limit(sql_query, query, query_type)
        corrected_sql = _enforce_simple_limit(corrected_sql, query, query_type)

        valid_gen, err_gen = validate_sql(connector, sql_query)
        valid_ref, err_ref = validate_sql(connector, corrected_sql)
        log("Retry Generated SQL Valid?", valid_gen)
        log("Retry Reflected SQL Valid?", valid_ref)

    candidates = []
    if valid_gen:
        try:
            gen_result = connector.execute_query(sql_query)
            candidates.append(("generator", sql_query, gen_result))
        except Exception as e:
            log("Generated SQL execution failed after validation", str(e))

    if valid_ref:
        try:
            ref_result = connector.execute_query(corrected_sql)
            candidates.append(("reflection", corrected_sql, ref_result))
        except Exception as e:
            log("Reflected SQL execution failed after validation", str(e))

    if not candidates:
        raise Exception(f"Both queries failed:\nGen: {err_gen}\nRef: {err_ref}")

    # Prioritize reflection, but if one returns rows and the other doesn't, pick the one with rows
    best = candidates[0]
    for source, candidate_sql, candidate_result in candidates:
        if len(candidate_result) > 0 and len(best[2]) == 0:
            best = (source, candidate_sql, candidate_result)
        elif source == "reflection" and len(candidate_result) > 0:
            best = (source, candidate_sql, candidate_result)

    selected_source, final_sql, result = best
    log("Selected SQL Source", selected_source)
    log("Execution Result", result)

    return {
        "sql": final_sql,
        "result": result
    }
