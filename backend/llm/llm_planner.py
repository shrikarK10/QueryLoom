
import requests
from utils.config import MODEL_NAME

OLLAMA_URL = "http://localhost:11434/api/generate"

def plan_query(question: str, tables: str, column_mapping: str):

    prompt = f"""
You are a query planner.

Your job is to extract ONLY the minimum required columns and conditions needed to answer the query.

---------------------

OUTPUT FORMAT (strict JSON ONLY):

{{
  "columns_needed": ["<col1>", "<col2>"],
  "conditions": "<filters or NONE>"
}}

---------------------

STRICT RULES:

1. ALWAYS use COLUMN MAPPING to verify columns exist. DO NOT guess.

2. ONLY include columns necessary for:
   - filtering (WHERE)
   - grouping (GROUP BY)
   - aggregation (SUM, COUNT, etc.)
   - final output

3. DO NOT include unnecessary columns
4. DO NOT list all columns of a table
5. DO NOT include table names anywhere in output

---------------------

INTENT HANDLING:

- "count", "how many" → use COUNT(column)
- "total", "sum" → use SUM(column)
- "average", "avg" → use AVG(column)
- "max", "highest" → MAX(column)
- "min", "lowest" → MIN(column)

- "per year", "per month", "by category" → include grouping column

---------------------

COLUMN RULES:

- NEVER invent columns
- Map natural language to real columns:
  - "name" → FirstName or Name (only if exists)
  - "price" → ListPrice
  - "sales" → TotalDue

- You MAY wrap columns in functions:
  - COUNT(CustomerID)
  - SUM(TotalDue)

---------------------

EXAMPLES:

Question: Top 5 most expensive products
Response:
{{
  "columns_needed": ["Name", "ListPrice"],
  "conditions": "NONE"
}}

---

Question: Customers from Seattle
Response:
{{
  "columns_needed": ["CustomerID", "City"],
  "conditions": "City = 'Seattle'"
}}

---

Question: Get sales per year
Response:
{{
  "columns_needed": ["OrderDate", "SUM(TotalDue)"],
  "conditions": "NONE"
}}

---------------------

COLUMN MAPPING:
{column_mapping}

---------------------

AVAILABLE TABLES:
{tables}

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
            "format": "json",
            "stream": False,
            "options": {
                "num_predict": 200,
                "temperature": 0.1
            }
        }
    )

    return response.json()["response"].strip()