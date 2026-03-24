from llm.sql_reflector import reflect_sql
from llm.sql_generator import generate_sql
from utils.logger import logger as log
from utils.sql_validator import validate_sql

def run_querymind(query: str, connector):
    log("User Query", query)

    schema = connector.get_schema()
    formatted_schema = ""
    for table, cols in schema.items():
        formatted_schema += f"\nTable: {table}\nColumns: {', '.join(cols)}\n"
    log("Schema Extracted", formatted_schema)

    sql_query = generate_sql(query, formatted_schema )
    log("Generated SQL", sql_query)

    corrected_sql = reflect_sql(query, formatted_schema, sql_query)
    log("Reflected SQL", corrected_sql)

    valid_gen, err_gen = validate_sql(connector, sql_query)
    valid_ref, err_ref = validate_sql(connector, corrected_sql)

    log("Generated SQL Valid?", valid_gen)
    log("Reflected SQL Valid?", valid_ref)

    # Step 4: Decision logic
    if valid_ref:
        final_sql = corrected_sql
        log("Using Reflected SQL")
    elif valid_gen:
        final_sql = sql_query
        log("Using Generated SQL")
    else:
        raise Exception(f"Both queries failed:\nGen: {err_gen}\nRef: {err_ref}")
    
    result = connector.execute_query(final_sql)
    log("Execution Result", result)

    return {
        "sql": corrected_sql,
        "result": result
    }