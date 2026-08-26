import sys
from pathlib import Path
import json

# Add backend to path
backend_dir = Path(__file__).resolve().parent
sys.path.append(str(backend_dir))

from connectors.sqlite_connector import SQLiteConnector
from schema.schema_catalog import SchemaCatalog
from schema.schema_retriever import SchemaRetriever
from utils.config import DB_PATH

def test_retriever():
    print(f"Connecting to database: {DB_PATH}\n")
    connector = SQLiteConnector(DB_PATH)
    catalog = SchemaCatalog(connector)
    retriever = SchemaRetriever(catalog)
    
    sample_queries = [
        "Show customers who purchased tracks",
        "Find customers by city",
        "Show product list price",
        "List all artists ordered alphabetically",
        "Find the genre with the highest number of purchases",
        "Most sold album"
        
    ]
    
    for query in sample_queries:
        print("=" * 80)
        print(f"QUERY: '{query}'")
        print("=" * 80)
        
        result = retriever.retrieve(query)
        
        # Display top tables (score > 0)
        matched_tables = [t for t in result["tables"] if t["score"] > 0]
        print(f"\n--- MATCHED TABLES ({len(matched_tables)}) ---")
        for t in matched_tables:
            terms = ", ".join(t['matched_terms'])
            reasons = "; ".join(t['reasons'])
            print(f"  - {t['table']:<20} | Score: {t['score']:<5} | Terms: [{terms}] | Reasons: {reasons}")

            
        # Display top columns (score > 0)
        matched_cols = [c for c in result["columns"] if c["score"] > 0]
        print(f"\n--- MATCHED COLUMNS ({len(matched_cols)}) ---")
        for c in matched_cols[:10]:
            terms = ", ".join(c['matched_terms'])
            reasons = "; ".join(c['reasons'])
            full_col = f"{c['table']}.{c['column']}"
            print(f"  - {full_col:<30} | Score: {c['score']:<5} | Terms: [{terms}] | Reasons: {reasons}")

            
        print("\n")

if __name__ == "__main__":
    test_retriever()
