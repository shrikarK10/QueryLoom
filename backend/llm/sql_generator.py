import requests
from pathlib import Path
from utils.config import MODEL_NAME , DATABASE_LANGUAGE
from utils.sql_cleaner import clean_sql_output
OLLAMA_URL = "http://localhost:11434/api/generate"
LOG_FILE = Path(__file__).resolve().parent / "generated_query_log.txt"


def generate_sql(question: str, schema: dict):

    prompt = f"""
You are an expert SQL generator.
DATABASE: {DATABASE_LANGUAGE}


You must follow these steps BEFORE writing SQL:

STEP 1: Identify relevant columns from the question
STEP 2: Find which tables contain those columns
STEP 3: If columns are in different tables → use JOIN
STEP 4: Generate the simplest correct query


You must follow these rules STRICTLY:

GENERAL RULES:
- Use ONLY the tables and columns provided in the schema
- DO NOT assume columns that are not listed
- Output ONLY raw SQL (no explanation, no markdown)
- Do NOT use ``` or any formatting
- SQL must be compatible with {DATABASE_LANGUAGE}


IMPORTANT:
- Do NOT overcomplicate queries
- Prefer simplest correct query

---------------------
SCHEMA:
{schema}

---------------------
RELATIONSHIPS (if needed):
Customer.CustomerID = CustomerAddress.CustomerID
CustomerAddress.AddressID = Address.AddressID
SalesOrderHeader.CustomerID = Customer.CustomerID
SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
SalesOrderDetail.ProductID = Product.ProductID
---------------------
EXAMPLE (SIMPLE_SELECT):

Question:
Top 5 most expensive products

SQL:
SELECT Name, ListPrice
FROM Product
ORDER BY ListPrice DESC
LIMIT 5;
---------------------
Question:
{question}

SQL:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"Prompt:\n{prompt}\n")
        log_file.write(f"Response:\n{response.json()['response'].strip()}\n")
        log_file.write("-" * 50 + "\n")
    
    raw_sql=response.json()["response"]
    return clean_sql_output(raw_sql)
