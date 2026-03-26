import re


def _convert_top_to_limit(sql: str) -> str:
    if re.search(r"\blimit\b", sql, flags=re.IGNORECASE):
        return sql

    match = re.match(r"(?is)^\s*select\s+top\s*\(?\s*(\d+)\s*\)?\s+", sql)
    if not match:
        return sql

    limit_n = match.group(1)
    sql = re.sub(r"(?is)^\s*select\s+top\s*\(?\s*\d+\s*\)?\s+", "SELECT ", sql, count=1)
    sql = sql.rstrip().rstrip(";") + f"\nLIMIT {limit_n};"
    return sql


def _normalize_null_checks(sql: str) -> str:
    sql = re.sub(r"(?i)\b([\w\.]+)\s*=\s*NULL\b", r"\1 IS NULL", sql)
    sql = re.sub(r"(?i)\b([\w\.]+)\s*(?:!=|<>)\s*NULL\b", r"\1 IS NOT NULL", sql)
    return sql


def clean_sql_output(text: str) -> str:
    sql = text.strip()

    # Extract SQL within <sql> tags if present
    match = re.search(r"(?is)<sql>\s*(.*?)\s*</sql>", sql)
    if match:
        sql = match.group(1).strip()

    if sql.startswith("```"):
        sql = re.sub(r"(?is)^```\s*sql\s*", "", sql)
        sql = sql.replace("```", "").strip()

    sql = re.sub(r"(?is)^\s*sql\s*[:\-]?\s*", "", sql).strip()
    sql = _convert_top_to_limit(sql)
    sql = _normalize_null_checks(sql)

    return sql