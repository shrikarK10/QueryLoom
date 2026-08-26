import sys
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).resolve().parent
sys.path.append(str(backend_dir))

from connectors.sqlite_connector import SQLiteConnector
from schema.schema_catalog import SchemaCatalog
from utils.config import DB_PATH

def test_schema_catalog():
    print(f"Connecting to database: {DB_PATH}")
    connector = SQLiteConnector(DB_PATH)
    
    catalog = SchemaCatalog(connector)
    
    tables = catalog.get_tables()
    print(f"Tables ({len(tables)}): {tables[:5]}...")
    assert len(tables) > 0, "No tables found in catalog"
    
    sample_table = tables[0]
    cols = catalog.get_columns(sample_table)
    print(f"Columns in '{sample_table}': {cols}")
    assert len(cols) > 0, f"No columns found in table {sample_table}"
    
    sample_col = cols[0]
    matched_tables = catalog.get_tables_for_column(sample_col)
    print(f"Tables for column '{sample_col}': {matched_tables}")
    assert sample_table in matched_tables, f"{sample_table} should be in matched tables for {sample_col}"
    
    assert catalog.has_table(sample_table), f"has_table({sample_table}) returned False"
    assert catalog.has_column(sample_table, sample_col), f"has_column({sample_table}, {sample_col}) returned False"
    assert not catalog.has_table("NonExistentTable_12345"), "has_table returned True for non-existent table"
    
    print("\n--- Summary of Catalog Data Structures ---")
    print(f"Raw Schema Type: {type(catalog.raw_schema)}")
    print(f"Formatted Schema snippet:\n{catalog.formatted_schema[:120].strip()}...")
    print(f"Column Mapping snippet:\n{catalog.column_mapping[:120].strip()}...")
    print(f"Relationships count: {len(catalog.relationships)}")
    print(f"Relationship Graph keys: {list(catalog.relationship_graph.keys())[:5]}")
    
    print("\n[SUCCESS] All SchemaCatalog unit tests passed!")


if __name__ == "__main__":
    test_schema_catalog()
