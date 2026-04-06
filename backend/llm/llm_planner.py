import requests
from utils.config import MODEL_NAME

OLLAMA_URL = "http://localhost:11434/api/generate"

def plan_query(question: str, tables: str, column_mapping: str):

    prompt = f"""
You are a query planner.

Your job is to select ONLY the minimum required tables and columns.

---------------------

OUTPUT FORMAT (strict JSON ONLY):
{{
  "tables_owning_columns": ["<table1_from_mapping>", "<table2_from_mapping>"],
  "bridging_tables_needed": ["<mapping_table>"],
  "entities": ["<table1>", "<table2>", "<mapping_table>"],
  "columns": ["<col1>", "<col2>"],
  "conditions": "<filters or NONE>",
  "join_required": "<YES or NO>"
}}

---------------------

STRICT RULES:

1. ALWAYS use the COLUMN MAPPING dictionary to verify which table contains a column! DO NOT guess!
2. ONLY include tables directly relevant to the question
3. DO NOT include generic or unrelated tables (like ErrorLog, BuildVersion)
4. DO NOT guess extra conditions
5. If query can be solved using ONE table → Join Required = NO
6. ONLY include columns explicitly needed

7. Detect query intent:
- "How many", "count" → use COUNT()
- "Total", "sum" → use SUM()
- "Average", "avg" → use AVG()

8. For COUNT queries:
- ONLY include one identifier column (like ID)
- DO NOT list all columns

9. DO NOT list all columns of a table
- Only include columns required to answer the question

10. DO NOT include unnecessary columns
- Only include columns needed for aggregation or grouping

12. Detect grouping queries:
- "per year", "per month", "by category" → GROUP BY
- Include grouping column (e.g., OrderDate for year)
- Include aggregation column (e.g., SUM(TotalDue))

13. NEVER invent column names 
- Use only columns that realistically exist in tables
- If unsure, choose the closest valid column

14. Entity Verification:
- You MUST list EVERY table that contains the columns you selected.
- If the columns exist in different tables, you MUST also list the bridging/mapping tables required to join them (e.g., CustomerAddress to join Customer and Address).
- DO NOT list a column if the table it belongs to is not in Entities.
EXAMPLES:

Question: Top 5 most expensive products
Response:
{{
  "tables_owning_columns": ["Product"],
  "bridging_tables_needed": [],
  "entities": ["Product"],
  "columns": ["Name", "ListPrice"],
  "conditions": "NONE",
  "join_required": "NO"
}}

---

Question: Customers from Seattle
Response:
{{
  "tables_owning_columns": ["Customer", "Address"],
  "bridging_tables_needed": ["CustomerAddress"],
  "entities": ["Customer", "Address", "CustomerAddress"],
  "columns": ["CustomerID", "City"],
  "conditions": "City = 'Seattle'",
  "join_required": "YES"
}}

---------------------

COLUMN MAPPING:
{column_mapping}

---------------------

Schema (For table relationships):
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
            "options": {"num_predict": 400,
            "temperature": 0.1,
            "top_p": 0.9,
            "repeat_penalty": 1.1}
        }
    )

    return response.json()["response"].strip()