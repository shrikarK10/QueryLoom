import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
LOG_FILE = Path(__file__).resolve().parent / "generated_query_log.txt"

def format_schema(schema: dict):
    formatted = ""
    for table, cols in schema.items():
        formatted += f"\nTable: {table}\nColumns: {', '.join(cols)}\n"
    return formatted


def generate_sql(question: str, schema: dict):
    formatted_schema = format_schema(schema)
    prompt = f"""
You are an expert SQL generator.

You must follow these rules STRICTLY:

1. Use ONLY the tables and columns provided in the schema
2. DO NOT assume columns that are not listed
3. If required data is not in a table, find the correct table and JOIN
4. Use explicit JOINs (no implicit joins)
5. Use correct aggregation and grouping when needed
6. Return ONLY SQL query (no explanation, no markdown)

---------------------
SCHEMA:
{formatted_schema}

---------------------
RELATIONSHIPS:
Customer.CustomerID = CustomerAddress.CustomerID
CustomerAddress.AddressID = Address.AddressID
SalesOrderHeader.CustomerID = Customer.CustomerID
SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
SalesOrderDetail.ProductID = Product.ProductID

---------------------
EXAMPLE:

Schema:
Customer(CustomerID, FirstName)
CustomerAddress(CustomerID, AddressID)
Address(AddressID, City)

Question:
List cities where customer name is John

SQL:
SELECT DISTINCT a.City
FROM Customer c
JOIN CustomerAddress ca ON c.CustomerID = ca.CustomerID
JOIN Address a ON ca.AddressID = a.AddressID
WHERE c.FirstName = 'John';

---------------------
NOW GENERATE SQL FOR:

Question:
{question}

SQL:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen2.5:7b-instruct-q4_K_M",
            "prompt": prompt,
            "stream": False
        }
    )

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"Prompt:\n{prompt}\n")
        log_file.write(f"Response:\n{response.json()['response'].strip()}\n")
        log_file.write("-" * 50 + "\n")
    
    return response.json()["response"].strip()