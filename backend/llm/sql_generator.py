import requests
from pathlib import Path
from utils.config import MODEL_NAME , DATABASE_LANGUAGE
from utils.sql_cleaner import clean_sql_output
OLLAMA_URL = "http://localhost:11434/api/generate"
LOG_FILE = Path(__file__).resolve().parent / "generated_query_log.txt"


def generate_sql(
    question: str,
    schema: str,
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
You are an expert SQL generator.

DATABASE: {DATABASE_LANGUAGE}
QUERY TYPE: {query_type}

---------------------
QUERY PLAN:
{query_plan}

---------------------
JOINS (MANDATORY USE):
{joins}

---------------------
SCHEMA:
{schema}

---------------------

{feedback_block}

---------------------

YOUR TASK:

- Generate SQL strictly based on:
  1. QUERY PLAN (columns_needed, conditions, requires_distinct, limit, aggregations, and ordering)
  2. PROVIDED JOINS

---------------------

- You MUST use the provided JOIN clauses EXACTLY as given
- DO NOT modify joins
- DO NOT invent joins
- DO NOT add new tables

- If requires_distinct is true, you MUST prepend DISTINCT to the SELECT clause (e.g. SELECT DISTINCT column1, column2...). This is critical to avoid duplicate rows.
- Use the limit specified in the QUERY PLAN if it is present
- Apply the sorting/ordering specified in the QUERY PLAN "ordering" array (using ORDER BY ... ASC/DESC)
- DO NOT assume columns
- DO NOT use COLUMN MAPPING
- You MUST use ONLY the provided JOIN clauses
- You are NOT allowed to create your own JOINs
- If JOIN is empty, use only single table
- Prefer simplest correct query
- DO NOT add unnecessary logic
- In SQLite, backslash (\) is treated as a literal character in string literals. Do NOT double-escape it (use 'adventure-works\pamela0', NOT 'adventure-works\\pamela0').
- Simple planner conditions must become direct WHERE predicates (e.g. WHERE ProductCategory.Name LIKE '%Bikes%'). Do NOT generate EXISTS, IN, or subqueries unless the query plan explicitly requires a subquery.
- When the intent is "sold", "purchased", "units", "quantity", or "copies" and the schema contains a quantity-type column (e.g. Quantity, OrderQty, Qty), aggregate with SUM(quantity_column) rather than COUNT(row_id). COUNT counts rows; SUM(Quantity) reflects actual units moved.
- When selecting a group key for aggregation results, prefer descriptive attributes (e.g. Name, Title, Description, CategoryName) over identifier columns (e.g. GenreId, ArtistId), when the question does not explicitly request IDs.

- SQL must be compatible with {DATABASE_LANGUAGE}


---------------------

OUTPUT FORMAT:

<thought>
Brief reasoning (1-2 lines max)
</thought>

<sql>
-- Do NOT output the text "FINAL SQL HERE". Output your actual SQL query directly.
SELECT ...
</sql>

---------------------

EXAMPLE:

<thought>
Using Product table, sorting by ListPrice, limiting to 5
</thought>

<sql>
SELECT Name, ListPrice
FROM Product
ORDER BY ListPrice DESC
LIMIT 5;
</sql>

---------------------

Question:
{question}

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