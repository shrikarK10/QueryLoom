def validate_sql(connector, sql: str):
    candidate = sql.strip().rstrip(";")
    if not candidate:
        return False, "SQL is empty"

    if not candidate.lower().startswith("select"):
        return False, "Only SELECT queries are allowed"

    try:
        connector.execute_query(f"EXPLAIN QUERY PLAN {candidate}")
        return True, None
    except Exception as e:
        return False, str(e)