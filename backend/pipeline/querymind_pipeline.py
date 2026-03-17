from llm.sql_generator import generate_sql
from utils.logger import logger as log

def run_querymind(query: str, connector):
    log("User Query", query)

    schema = connector.get_schema()
    log("Schema Extracted", schema)

    sql_query = generate_sql(query, schema)
    log("Generated SQL", sql_query)

    result = connector.execute_query(sql_query)
    log("Execution Result", result)

    return {
        "sql": sql_query,
        "result": result
    }