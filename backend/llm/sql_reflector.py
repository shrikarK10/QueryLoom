import requests
from utils.config import MODEL_NAME, DATABASE_LANGUAGE
from utils.sql_cleaner import clean_sql_output

OLLAMA_URL = "http://localhost:11434/api/generate"

def reflect_sql(
    question: str,
    schema: str,
    sql_query: str,
    column_mapping: str,
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
You are an expert SQL auditor and fixer.

DATABASE: {DATABASE_LANGUAGE}
QUERY TYPE: {query_type}

---------------------
COLUMN MAPPING:
{column_mapping}

---------------------
SCHEMA:
{schema}

---------------------

Your job is to VALIDATE and CORRECT the SQL query.

STRICT PROCESS:

STEP 1: Identify columns used in SQL (SELECT, WHERE, JOIN)

STEP 2: For EACH column:
- Verify it exists in the table used
- If NOT → use COLUMN MAPPING to find correct table

STEP 3: If column belongs to different table:
- ADD correct JOIN
- FIX query

STEP 4: Validate logic:
- Avoid duplicate rows from joins
- Fix aggregation issues
- Fix COUNT problems

STEP 5: Validate SQL:
- All aliases must be defined
- No invalid column references
- Query must execute successfully

STEP 6: Schema Validation

- Remove any table not present in SCHEMA
- Remove any column not present in SCHEMA
- Replace with correct table using COLUMN MAPPING
---------------------

{feedback_block}

IMPORTANT RULES:

- If SQL is correct → RETURN AS IS
- DO NOT overcomplicate
- DO NOT add unnecessary joins
- Prefer simplest correct query
- Keep business logic aligned with the user question (avoid unrelated filters)

- Output format MUST explicitly use <thought> and <sql> tags
- First, write a <thought> block explaining your fixes and reasoning
- Then, output ONLY the raw SQL inside a <sql> block

---------------------
STRICT SCHEMA CONSTRAINT:

- You are ONLY allowed to use tables listed in SCHEMA
- You are ONLY allowed to use columns listed in SCHEMA
- DO NOT invent tables (e.g., City, AddressType, etc.)
- DO NOT invent columns
- If something is not in schema → it DOES NOT exist

If you use any table or column not in schema → the query is INVALID
---------------------
QUESTION:
{question}

---------------------
SQL TO REVIEW:
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