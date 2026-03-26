import sys
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).resolve().parent
sys.path.append(str(backend_dir))

from connectors.sqlite_connector import SQLiteConnector
from pipeline.querymind_pipeline import run_querymind
from utils.config import DB_PATH

def main():
    connector = SQLiteConnector(DB_PATH)
    
    test_queries = [
        "What are the top 5 most expensive products?",
        "How many employees do we have?",
        "List all products that cost more than 1000",
        "Which city has the most addresses?"
    ]
    
    for i, q in enumerate(test_queries, 1):
        print(f"\n[{i}/{len(test_queries)}] Testing Query: {q}")
        try:
            result = run_querymind(q, connector)
            print("\n>> Selected SQL:")
            print(result.get("sql", "None"))
            print(f"\n>> Row count returned: {len(result.get('result', []))}")
            if result.get('result'):
                print(f">> First row data: {result['result'][0]}")
        except Exception as e:
            print(f"\n!! Error testing query '{q}': {e}")

if __name__ == "__main__":
    main()
