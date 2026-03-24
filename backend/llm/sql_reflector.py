import requests
from utils.config import MODEL_NAME, DATABASE_LANGUAGE
from utils.sql_cleaner import clean_sql_output

OLLAMA_URL = "http://localhost:11434/api/generate"

def reflect_sql(question: str, schema: str, sql_query: str):
    prompt = f"""
You are an expert SQL auditor and fixer.

Your job is to VALIDATE and CORRECT the SQL query.

---------------------
DATABASE:
{DATABASE_LANGUAGE}

---------------------
STRICT PROCESS (follow in order):

STEP 1: Identify required columns from the question

STEP 2: Verify those columns exist in the schema
- If a column is used from the wrong table → FIX it
- If column is missing → find correct table

STEP 3: Check if JOIN is required
- If columns come from multiple tables → ADD correct JOINs
- If JOIN is unnecessary → REMOVE it

STEP 4: Validate logic
- Avoid duplicate rows due to joins
- Use DISTINCT or proper grouping if needed
- Fix incorrect COUNT logic

STEP 5: Validate SQL correctness
- All table aliases must be defined
- No invalid column references
- SQL must run without errors

---------------------
IMPORTANT RULES:

- If the SQL is already correct → RETURN IT AS IS
- DO NOT add unnecessary joins
- DO NOT increase complexity
- Prefer the simplest correct query

- Output ONLY raw SQL
- NO markdown
- NO explanation
- SQL must be compatible with {DATABASE_LANGUAGE}

---------------------
SCHEMA:
{schema}

---------------------
QUESTION:
{question}

---------------------
SQL TO REVIEW:
{sql_query}

---------------------
FINAL SQL:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {"num_predict": 150}
        }
    )

    raw_sql = response.json()["response"]
    return clean_sql_output(raw_sql)