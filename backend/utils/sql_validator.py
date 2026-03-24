def validate_sql(connector, sql: str):
    try:
        connector.execute_query(sql)
        return True, None
    except Exception as e:
        return False, str(e)