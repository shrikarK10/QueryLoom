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

- You MUST preserve the provided JOIN logic
- Only fix:
  • syntax errors
  • wrong column usage
  • aggregation mistakes
  • missing GROUP BY
  • incorrect filters

- Ensure query aligns with QUERY PLAN

- Keep query SIMPLE and correct

---------------------

OUTPUT FORMAT:

<thought>
Brief reasoning (1-2 lines)
</thought>

<sql>
FINAL SQL HERE
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