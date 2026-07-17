
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
  "columns_needed": ["Table.Column"],
  "conditions": ["Table.Column = Value"],
  "requires_distinct": boolean,
  "limit": int | null,
  "aggregations": [
    {{
      "function": "COUNT | SUM | AVG | MIN | MAX",
      "column": "Table.Column",
      "distinct": boolean
    }}
  ],
  "ordering": [
    {{
      "column": "Table.Column",
      "direction": "ASC | DESC"
    }}
  ]
}}

---------------------

STRICT RULES:

1. ALWAYS use COLUMN MAPPING to verify columns exist. DO NOT guess.
2. ALWAYS prefix every column name with its table name (e.g., Table.Column). Fully qualify all columns inside "columns_needed", "conditions", "aggregations", and "ordering".
3. ONLY include columns in "columns_needed" that are explicitly requested to appear in the final answer. Do NOT include join keys, IDs, or helper columns unless the user explicitly asks for them.
4. Do NOT add columns that are not directly needed to answer the question. Only include additional columns if they are required by an aggregation. If the question explicitly mentions "ID" or "IDs", prefer columns ending in ID (e.g., SalesOrderID) over other coexisting columns like SalesOrderNumber.
5. Conditions must contain only simple field-to-value comparisons (e.g., "ProductCategory.Name LIKE '%Bikes%'"). Do NOT generate JOINs, subqueries, EXISTS, IN, or nested SQL inside conditions. The pipeline resolves table joins automatically. For example, to filter by categories containing 'Bikes', just write "ProductCategory.Name LIKE '%Bikes%'" and NEVER write an EXISTS subquery.
6. Only infer grouping when the question explicitly indicates grouping (e.g. "per", "for each", "grouped by", "by category", "by year"). Otherwise assume the aggregation is global. Do NOT add grouping columns (like ProductID) for global aggregates.
7. When a full person name is provided: map the first token to FirstName and the last token to LastName (e.g., "Orlando Gee" -> "Customer.FirstName = 'Orlando'", "Customer.LastName = 'Gee'"). Do not infer Title or Suffix unless explicitly mentioned.
8. Convert descriptive phrases into their corresponding schema values:
   - "shipping address" -> "CustomerAddress.AddressType = 'Shipping'"
   - "billing address" -> "CustomerAddress.AddressType = 'Billing'"
   - "shipping address of an order" -> "SalesOrderHeader.ShipToAddressID = Address.AddressID"
   - "billing address of an order" -> "SalesOrderHeader.BillToAddressID = Address.AddressID"
9. Infer ordering only when explicitly requested (e.g. "top", "highest", "largest" -> direction is DESC; "lowest", "smallest" -> direction is ASC). Specify columns and direction in the "ordering" list.
10. Set "requires_distinct" to true if the question asks for unique/distinct list of values, OR if it asks for a list of parent entities (e.g., "customers", "products", "categories") that are retrieved from a one-to-many relationship (like orders/order details) to avoid duplicate rows.
11. Set "limit" to the integer limit requested (e.g. top N, first N), or null if there is no explicit limit.
12. Words like "top", "most expensive", "highest priced", "lowest priced", "largest" imply ORDER BY (+ LIMIT if applicable), NOT MAX()/MIN() aggregation.
13. MAX/MIN only when asking for: maximum, minimum, highest value, lowest value, largest amount (e.g., "What is the highest list price?").
14. If all required columns and conditions come from one table, do not infer additional tables in the plan.
15. When generating counts or sums per group (e.g., count of products in each category), default to sorting by the count or sum descending (direction DESC) in the "ordering" list, unless another ordering is explicitly requested.
16. For queries involving HAVING filters or aggregate conditions (e.g., "sold more than 5 times total", "spent more than 100"), always include the aggregate column in "columns_needed" (or specify the aggregation in "aggregations" and ensure it is selected) so the query outputs the calculated sum/count/etc. alongside the group key.

---------------------

INTENT HANDLING:

- For aggregations:
  - "count", "how many" -> function is COUNT, distinct is true if counting unique items (e.g., unique customers)
  - "total", "sum", "spent", "revenue" -> function is SUM
  - "average", "avg" -> function is AVG
  - "max", "highest" -> function is MAX (ONLY when asking for a single maximum value). Note: "highest total" means SUM aggregation ordered DESC with LIMIT 1.
  - "min", "lowest" -> function is MIN (ONLY when asking for a single minimum value)

- When the question refers to "sold", "purchased", "units", "quantity", or "copies", and the schema contains a quantity-type column (e.g. Quantity, OrderQty, Qty): prefer SUM(quantity_column) over COUNT(row_id). COUNT counts the number of invoice lines; SUM(Quantity) reflects the actual number of units moved.

- When grouping results, prefer descriptive attributes (e.g. Name, Title, Description, CategoryName) over identifier columns (e.g. GenreId, ArtistId) in "columns_needed", when the question does not explicitly request IDs.

- "per year", "per month", "by category" → include grouping column in columns_needed

---------------------

EXAMPLES:

Question: Top 5 most expensive products
Response:
{{
  "columns_needed": ["Product.Name", "Product.ListPrice"],
  "conditions": [],
  "requires_distinct": false,
  "limit": 5,
  "aggregations": [],
  "ordering": [
    {{
      "column": "Product.ListPrice",
      "direction": "DESC"
    }}
  ]
}}

---

Question: Customers from Seattle
Response:
{{
  "columns_needed": ["Customer.FirstName", "Customer.LastName", "Address.City"],
  "conditions": ["Address.City = 'Seattle'"],
  "requires_distinct": false,
  "limit": null,
  "aggregations": [],
  "ordering": []
}}

---

Question: Get sales per year
Response:
{{
  "columns_needed": ["SalesOrderHeader.OrderDate"],
  "conditions": [],
  "requires_distinct": false,
  "limit": null,
  "aggregations": [
    {{
      "function": "SUM",
      "column": "SalesOrderHeader.TotalDue",
      "distinct": false
    }}
  ],
  "ordering": []
}}

---

Question: Show the FirstName and LastName of all customers who have ordered products from a ProductCategory with name containing 'Bikes'
Response:
{{
  "columns_needed": ["Customer.FirstName", "Customer.LastName"],
  "conditions": ["ProductCategory.Name LIKE '%Bikes%'"],
  "requires_distinct": true,
  "limit": null,
  "aggregations": [],
  "ordering": []
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