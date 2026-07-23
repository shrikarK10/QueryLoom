# QueryLoom

QueryLoom is a hybrid, AI-powered Text-to-SQL system designed to translate natural language questions into precise, executable SQL queries. 

Unlike purely prompt-driven architectures, QueryLoom couples Large Language Models (LLMs) with deterministic graph-based algorithms to guarantee structurally sound joins, eliminate column/table hallucinations, and automatically heal query syntax errors before database execution.

---

<p align="center">
  <a href="https://github.com/shrikarK10/QueryLoom/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/shrikarK10/QueryLoom?style=for-the-badge&color=blue" alt="License: MIT">
  </a>
  <a href="https://github.com/shrikarK10/QueryLoom/stargazers">
    <img src="https://img.shields.io/github/stars/shrikarK10/QueryLoom?style=for-the-badge&color=gold" alt="GitHub Stars">
  </a>
  <a href="https://github.com/shrikarK10/QueryLoom/issues">
    <img src="https://img.shields.io/github/issues/shrikarK10/QueryLoom?style=for-the-badge&color=red" alt="GitHub Issues">
  </a>
  <br />
  <a href="https://fastapi.tiangolo.com">
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  </a>
  <a href="https://ollama.com">
    <img src="https://img.shields.io/badge/Ollama-Qwen2.5-000000?style=for-the-badge" alt="Ollama/Qwen2.5">
  </a>
</p>

---

##  Motivation: Why QueryLoom?

Standard Text-to-SQL applications rely entirely on massive system prompts to guide LLMs through complex database schemas. While LLMs are excellent at semantic understanding and logical breakdown, this "pure prompting" approach frequently suffers from critical production failures:

1. **Schema Hallucination:** Inventing columns or referencing tables that do not exist.
2. **Join-Path Failures:** Building incorrect, missing, or convoluted `JOIN` conditions, especially across complex many-to-many schemas.
3. **Execution Errors:** Generating syntax that the local SQL dialect cannot parse.
4. **Overfitting:** Performing well on the primary database but completely breaking when applied to an unseen database.

**QueryLoom** addresses these bottlenecks with a **hybrid architecture**:
- **LLMs** handle reasoning: classification, query intent planning, SQL generation, and reflection.
- **Deterministic Code** handles data structures: dynamic relationship graph construction, shortest join path resolution (via Dijkstra's algorithm), deterministic plan repairs, and query syntax validation.

---

##  Core Features

- **Multi-Agent Pipeline:** Features a structured **Planner → Generator → Reflector** multi-agent cascade for parsing intent, writing queries, and refining syntax.
- **Dynamic Schema Extraction & Repair:** Dynamically inspects table schemas to automatically map and correct column hallucinations.
- **Deterministic Join Resolution:** Converts database foreign keys into a relationship graph and uses Dijkstra's shortest-path algorithm to construct `JOIN` conditions.
- **Self-Healing Loop:** Automatically captures validation errors (`EXPLAIN QUERY PLAN`) and feeds them back to the LLM agents for automated correction.
- **Cross-Database Evaluation Framework:** Evaluates performance against both seen (`AdventureWorks`) and unseen (`Chinook`) database schemas out-of-the-box.
- **Semantic & Strict Evaluation:** Uses strict record matching alongside semantic partial-matching to accurately assess generated query utility.
- **Local Inference:** Built on Ollama, enabling private, locally-hosted execution using open-weights models (e.g., `qwen2.5`).

---

##  Architecture Overview

QueryLoom splits execution into semantic parsing (using an LLM) and relational stitching (using graph algorithms).

```
                      ┌──────────────────────┐
                      │      User Query      │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │ Query Classification │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │  Schema Extraction   │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │  Relationship Graph  │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │    Planner (LLM)     │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │ Deterministic Join   │
                      │   Path Resolution    │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │   Generator (LLM)    │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │   Reflector (LLM)    │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │    SQL Validation    │◄───┐
                      └──────────┬───────────┘    │
                                 │                │
                        [Valid?] ├─No─────────┐   │ (Retry with
                                 │            │   │  DB Feedback)
                                Yes           ▼   │
                                 │       ┌────────┴─┐
                                 │       │  Retry   │
                                 │       │  Loop    │
                                 │       └──────────┘
                                 ▼
                      ┌──────────────────────┐
                      │    SQL Execution     │
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │    Final Results     │
                      └──────────────────────┘
```

### Demonstration & Architecture Artifacts

*A high-level animation of QueryLoom processing a complex analytical query and returning data:*

![QueryLoom Demo Overview](assets/demo.gif)

*Component layout showing the separation between LLM-based logic and deterministic logic:*

![QueryLoom Core Architecture](assets/architecture.png)

---

## Example Run: Query & Generated SQL

To demonstrate the hybrid execution flow, consider the following question run on the **AdventureWorks** database:

### Question
> *"List the names of products in the 'Bikes' category that have been sold more than 5 times total."*

### 1. Planner Output (LLM)
The Planner parses the natural language question and outputs a clean JSON schema, verifying columns against database dictionary schemas:
```json
{
  "columns_needed": ["Product.Name"],
  "conditions": ["ProductCategory.Name LIKE '%Bikes%'"],
  "requires_distinct": false,
  "limit": null,
  "aggregations": [
    {
      "function": "SUM",
      "column": "SalesOrderDetail.OrderQty",
      "distinct": false
    }
  ],
  "ordering": [
    {
      "column": "SalesOrderDetail.OrderQty",
      "direction": "DESC"
    }
  ]
}
```

### 2. Join Path Resolution (Deterministic)
The system notices that the columns span three separate tables: `Product`, `ProductCategory`, and `SalesOrderDetail`.
Using Dijkstra's algorithm over the dynamically extracted relationship graph, the engine resolves the shortest path:
$$\text{ProductCategory} \longleftrightarrow \text{Product} \longleftrightarrow \text{SalesOrderDetail}$$

It automatically generates the exact JOIN statements:
```sql
JOIN Product ON ProductCategory.ProductCategoryID = Product.ProductCategoryID
JOIN SalesOrderDetail ON Product.ProductID = SalesOrderDetail.ProductID
```

### 3. Generator & Reflector SQL (LLM + Verification)
The Generator integrates the plan with the joins, and the Reflector cleans up group key mismatches to output:
```sql
SELECT Product.Name, SUM(SalesOrderDetail.OrderQty) AS TotalQuantity
FROM ProductCategory
JOIN Product ON ProductCategory.ProductCategoryID = Product.ProductCategoryID
JOIN SalesOrderDetail ON Product.ProductID = SalesOrderDetail.ProductID
WHERE ProductCategory.Name LIKE '%Bikes%'
GROUP BY Product.Name
HAVING SUM(SalesOrderDetail.OrderQty) > 5
ORDER BY TotalQuantity DESC;
```

---

## Evaluation Results

QueryLoom was thoroughly benchmarked on two SQLite databases. Performance numbers demonstrate that the system **generalizes effectively to unseen schemas** without overfitting.

### 1. AdventureWorks Database (Seen Schema)
*A complex corporate ERP schema with multi-tier hierarchies and extensive relationships.*

| Metric | Result | Detail |
| :--- | :---: | :--- |
| **Total Test Queries** | 50 | Across Simple, Medium, and Hard difficulties |
| **Strict Accuracy** | **88.00%** | Requires exact match of query execution datasets |
| **Semantic Accuracy** | **94.00%** | Partial match of key columns and record counts |
| **Average Latency** | ~12.68s | Local inference using Ollama with Qwen2.5 |

#### AdventureWorks Difficulty Breakdown
| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |
| :--- | :---: | :---: | :---: | :---: |
| **Simple** | 15 | 14 | 0 | 93.33% |
| **Medium** | 20 | 18 | 0 | 90.00% |
| **Hard** | 15 | 12 | 3 | 100.00% |

### 2. Chinook Database (Unseen Schema)
*A media store database containing track lists, artists, invoices, and employee records. The model was evaluated without schema-specific instructions or examples.*

| Metric | Result | Detail |
| :--- | :---: | :--- |
| **Total Test Queries** | 30 | Evaluates zero-shot generalization capabilities |
| **Strict Accuracy** | **76.67%** | Strict dataset identity matching |
| **Semantic Accuracy** | **90.00%** | Returns the correct entities and primary keys |
| **Average Latency** | ~13.13s | Zero schema-specific fine-tuning or prompting |

#### Chinook Difficulty Breakdown
| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |
| :--- | :---: | :---: | :---: | :---: |
| **Simple** | 10 | 7 | 2 | 90.00% |
| **Medium** | 10 | 9 | 1 | 100.00% |
| **Hard** | 10 | 7 | 1 | 80.00% |

---

## Project Evolution

```
┌────────────────────────────────┐
│             v0.1               │ Pure LLM-based Text-to-SQL prototype.
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│             v1.0               │ Hybrid deterministic graph-based JOINs.
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│             v1.1               │ Cross-database evaluation & self-healing.
└────────────────────────────────┘
```

- **v0.1**: Initial prototype relying entirely on zero-shot prompting. High rate of hallucinations and syntax errors.
- **v1.0**: Introduction of the hybrid architecture. Planner/Generator splits, custom Dijkstra-based shortest-path JOIN resolver, and schema-based column repair.
- **v1.1** (Current): Cross-database testing support (Chinook, AdventureWorks), API endpoint deployment with FastAPI, self-healing retries with `EXPLAIN QUERY PLAN` validation, and standardized evaluations.

---

## Installation

### Prerequisites
- Python 3.10 or 3.11
- [Ollama](https://ollama.com) installed and running locally.

### Step 1: Clone the Repository
```bash
git clone https://github.com/shrikarK10/QueryLoom.git
cd QueryLoom
```

### Step 2: Set Up Environment & Install Dependencies
Create a virtual environment and install the required modules:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/macOS
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Step 3: Configure local LLM
Pull the target reasoning model using Ollama:
```bash
ollama pull qwen2.5
```
*(Verify connection using `python llm_tetser.py`)*

---

## Usage

### 1. Launching the API Server
Run the FastAPI application from the `backend` directory using Uvicorn:
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 2. Querying the Endpoint
You can interact with the API by posting a natural language question. The backend automatically targets the database configured in `backend/utils/config.py`.

#### cURL Request
```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d "{\"query\": \"What are the top 5 most expensive products?\"}"
```

#### Python Request Client
```python
import requests

url = "http://localhost:8000/query"
payload = {"query": "List all products that cost more than 1000"}

response = requests.post(url, json=payload)
data = response.json()

print(f"SQL Query: {data['sql']}")
print(f"Results: {data['result']}")
```

### 3. Running Evaluations
To run evaluation suites against the active database:
```bash
python evaluation_runner.py
```
To toggle between databases, change the active SQLite database path configuration within [config.py](file:///c:/Projects/Projects/QueryLoom/QueryLoom/backend/utils/config.py).

### 4. Direct CLI Test Runner
Run a quick, pre-configured list of test queries from the command line:
```bash
python run_tests.py
```

---

## Project Structure

```
QueryLoom/
├── backend/
│   ├── api/
│   │   ├── routes.py                 # FastAPI routing endpoints
│   │   ├── test.py                   # Ad-hoc query test script
│   │   ├── AdventureWorks-sqlite.db  # SQLite database for AdventureWorks
│   │   └── Chinook_Sqlite.sqlite     # SQLite database for Chinook
│   ├── connectors/
│   │   ├── base_connector.py         # Abstract DB connector interface
│   │   └── sqlite_connector.py       # SQLite concrete implementation
│   ├── llm/
│   │   ├── llm_planner.py            # Planner: parses query into intermediate plan
│   │   ├── sql_generator.py          # Generator: writes query from plan + joins
│   │   └── sql_reflector.py          # Reflector: reviews and repairs output SQL
│   ├── pipeline/
│   │   └── querymind_pipeline.py     # Core hybrid executor coordination pipeline
│   ├── utils/
│   │   ├── column_mapper.py          # Builds column-to-table schemas
│   │   ├── config.py                 # Core configurations (model names, active DB)
│   │   ├── logger.py                 # Custom logger configuration
│   │   ├── relationship_extractor.py # FK extraction and Dijkstra path resolution
│   │   ├── schema_updater.py         # Formats schema contexts for LLM prompts
│   │   └── sql_validator.py          # Syntax check using EXPLAIN QUERY PLAN
│   ├── evaluation_dataset.json       # AdventureWorks evaluation test suite
│   ├── evaluation_dataset_chinook.json # Chinook evaluation test suite
│   ├── evaluation_runner.py          # Test suite executor and markdown reporter
│   ├── main.py                       # FastAPI entry point
│   └── run_tests.py                  # CLI test runner
├── requirements.txt                  # Python dependencies
├── llm_tetser.py                     # Connection checker for local Ollama
└── README.md                         # Project documentation
```

---

## Current Limitations

- **SELECT Operations Only:** The engine restricts inputs to read-only queries by validating that SQL queries begin with `SELECT` and running `EXPLAIN QUERY PLAN` prior to actual database execution.
- **Dialect Specificity:** The system uses SQLite constructs (e.g., `strftime` and `LIMIT` syntax). Generalizing to other dialects requires extending connector formatting.
- **Graph Dependency:** The path resolver relies on defined Foreign Keys. Databases with missing relationships or dynamic schemas require manual definition or semantic enrichment.
- **Inference Speed:** Average latency sits around ~12-13 seconds, which is bounded by local LLM CPU/GPU generation speeds on Ollama.

---

## Roadmap

- [ ] **Multi-Dialect Support:** Extend connectors to support PostgreSQL, MySQL, and BigQuery.
- [ ] **Semantic Schema Enrichment:** Support graph relationship inference for databases lacking explicit foreign keys (using semantic text alignment of column names).
- [ ] **Vectordb Schema Pruning:** Integrate a vector store to retrieve and load only relevant sub-sections of schemas, allowing the system to scale to databases containing thousands of tables.
- [ ] **Interactive UI Console:** Create a lightweight web interface for executing queries, visualizing database tables, and inspecting intermediate plans.

---

## Contributing

Contributions are welcome! Please follow these steps to propose changes:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## Citation

If you use this system or hybrid concept in research, please cite:

```bibtex
@software{queryloom2026,
  author = {ShrikarK10},
  title = {QueryLoom: Hybrid Deterministic & LLM-Powered Text-to-SQL Pipeline},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/shrikarK10/QueryLoom}}
}
```
