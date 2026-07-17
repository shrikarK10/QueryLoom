import requests
from utils.config import MODEL_NAME, DATABASE_LANGUAGE
from utils.sql_cleaner import clean_sql_output

OLLAMA_URL = "http://localhost:11434/api/generate"

def reflect_sql(
    question: str,
    schema: str,
    sql_query: str,
    column_mapping: str,
    query_plan: str,
    joins: str,
    query_type: str = "GENERAL",
    previous_error: str | None = None
):

    feedback_block = ""
    if previous_error:
        feedback_block = f"""
LAST ERROR FROM DB/VALIDATOR:
{previous_error}

Use this error to repair the SQL.
"""

    prompt = f"""
You are an expert SQL fixer.

DATABASE: {DATABASE_LANGUAGE}
QUERY TYPE: {query_type}

---------------------
QUERY PLAN:
{query_plan}

---------------------
EXPECTED JOINS (DO NOT MODIFY):
{joins}

---------------------
SCHEMA:
{schema}

---------------------

Your job is to FIX the SQL query if needed.

---------------------

{feedback_block}

---------------------

STRICT RULES:

- DO NOT change JOIN structure unless it is completely invalid
- DO NOT add new tables
- DO NOT invent columns

- If requires_distinct is true in the QUERY PLAN, you MUST ensure that the SQL query uses DISTINCT in its SELECT clause (e.g. SELECT DISTINCT ...). If it is missing, you MUST correct it to include DISTINCT.
- Ensure any limit specified in the QUERY PLAN is properly applied in the SQL
- Ensure any ordering/sorting specified in the QUERY PLAN "ordering" array is correctly implemented in the SQL (using ORDER BY)
- Only fix:
  • syntax errors
  • wrong column usage
  • aggregation mistakes
  • missing GROUP BY
  • incorrect filters

- Ensure query aligns with QUERY PLAN (including columns_needed, conditions, requires_distinct, limit, aggregations, and ordering)
- In SQLite, backslash (\) is treated as a literal character in string literals. Do NOT double-escape it (use 'adventure-works\pamela0', NOT 'adventure-works\\pamela0').
- If all required columns and conditions come from a single table, simplify the query by removing any unnecessary JOIN clauses.
- Remove uncorrelated EXISTS clauses. Simplify subqueries/EXISTS clauses into direct flat WHERE clauses on the joined tables where possible.
- If the query intent is "sold", "purchased", "units", "quantity", or "copies" and the generated SQL aggregates with COUNT(row_id) instead of SUM(quantity_column), correct it to SUM(quantity_column). Example: COUNT(InvoiceLineId) → SUM(Quantity).
- If a GROUP BY uses an identifier column (e.g. GenreId, ArtistId) but the SELECT outputs that same identifier instead of its descriptive attribute, correct the SELECT to output the descriptive attribute (e.g. Name, Title, Description, CategoryName) — when the question does not explicitly request IDs.

- Keep query SIMPLE and correct


---------------------

OUTPUT FORMAT:

<thought>
Brief reasoning (1-2 lines)
</thought>

<sql>
-- Do NOT output the text "FINAL SQL HERE". Output your actual SQL query directly.
SELECT ...
</sql>

---------------------

QUESTION:
{question}

---------------------
SQL:
{sql_query}

---------------------
Response:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 400,
                "temperature": 0.1,
                "top_p": 0.9,
                "repeat_penalty": 1.1
            }
        },
        timeout=60
    )
    response.raise_for_status()

    raw_sql = response.json()["response"]
    return clean_sql_output(raw_sql)