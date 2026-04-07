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
COLUMN MAPPING:
{column_mapping}

---------------------
QUERY PLAN:
{query_plan}

---------------------
SCHEMA:
{schema}

---------------------

You must follow these steps BEFORE writing SQL:

STEP 1: Refer to the QUERY PLAN to know exactly what entities, columns, and conditions are needed.
STEP 2: Use COLUMN MAPPING to find correct tables.
STEP 3: If columns belong to different tables → use JOIN.
STEP 4: Generate the simplest correct query matching the plan.

{feedback_block}

---------------------

STRICT RULES:

- Use ONLY tables and columns from schema
- DO NOT assume columns
- If a column is not in a table → use mapping to find correct table
- DO NOT guess column locations

- Prefer simplest correct query
- DO NOT overuse JOINs
- DO NOT add unnecessary tables
- ALWAYS prefer direct JOINs (e.g., ON a.CustomerID = b.CustomerID) over using intermediate bridging tables (like Address) if a direct relationship exists.
- Properly map analytical intents (like ranking, running totals, partitioning) to the correct SQL window functions (e.g., RANK(), DENSE_RANK(), OVER()) rather than basic analytical workarounds.

- First, write a <thought> block explaining your reasoning.
- Then, output ONLY the raw SQL inside a <sql> block.
- DO NOT use markdown code blocks like ```sql inside the <sql> tag. The <sql> tag should directly contain the query.
- SQL must be compatible with {DATABASE_LANGUAGE}

---------------------
STRICT SCHEMA CONSTRAINT:

- You are ONLY allowed to use tables and columns listed in SCHEMA
- DO NOT invent tables or columns
- If you use any table or column not in schema → the query is INVALID

---------------------
Before writing SQL:

- Verify every table used exists in SCHEMA
- Verify every column used exists in that table
---------------------


EXAMPLE:

Question:
Top 5 most expensive products

Response:
<thought>
The question asks for the top 5 most expensive products.
I need the `Name` and `ListPrice` columns from the `Product` table.
I will order by `ListPrice` descending and limit to 5.
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