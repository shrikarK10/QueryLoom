def clean_sql_output(text: str) -> str:
    text = text.strip()

    # remove markdown
    if text.startswith("```"):
        text = text.replace("```sql", "").replace("```", "").strip()

    # remove accidental prefixes
    if text.lower().startswith("sql"):
        text = text[3:].strip()

    return text