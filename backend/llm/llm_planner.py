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
5. join_required logic:
- If the "entities" array contains EXACTLY 1 table → "join_required": "NO"
- If the "entities" array contains 2 OR MORE tables → "join_required": "YES"

6. ONLY include columns explicitly needed

7. Detect query intent and map semantic meaning to corresponding SQL functions:
- Aggregation: "Total", "sum" → SUM() | "Average", "avg", "mean" → AVG() | "Count", "how many" → COUNT() | "Min", "lowest" → MIN() | "Max", "highest" → MAX()
- Window/Analytical: "Rank", "ranking" → RANK() OVER() | "Running total", "cumulative" → SUM() OVER() | "Difference", "previous" → LAG() or LEAD()
- Date Extraction: "Year of", "monthly", "daily" → extraction functions (e.g. YEAR(), MONTH()) or STRFTIME

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

13. NEVER invent base column names 
- Base columns MUST realistically exist in tables.
- However, you are ALLOWED AND ENCOURAGED to wrap valid columns in SQL functions in the "columns" list (e.g., "RANK() OVER(ORDER BY SUM(TotalDue) DESC)", "SUM(TotalDue)").

14. Entity Verification:
- You MUST list EVERY table that contains the columns you selected.
- If the columns exist in different tables, you MUST list the bridging tables required to join them IF AND ONLY IF they cannot be joined directly.
- STRICT RULE: If two tables share a direct key (e.g., CustomerID exists in both Customer and SalesOrderHeader), DO NOT add a bridging table.
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