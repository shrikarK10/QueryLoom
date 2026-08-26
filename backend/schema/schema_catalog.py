from utils.schema_updater import format_schema, build_column_mapping
from utils.relationship_extractor import (
    extract_relationships,
    build_relationship_graph
)


class SchemaCatalog:
    """
    Central representation of a database schema.

    Builds and stores existing QueryMind schema structures:
    - raw_schema: dict[str, list[str]]
    - formatted_schema: str
    - column_mapping: str
    - relationships: list[dict]
    - relationship_graph: defaultdict(list)
    """

    def __init__(self, connector):
        self.connector = connector

        # Raw schema returned by database connector (dict[table_name, list[column_name]])
        self.raw_schema = connector.get_schema()

        # Schema string representations
        self.formatted_schema = format_schema(self.raw_schema)
        self.column_mapping = build_column_mapping(self.raw_schema)

        # Database relationships and graph
        self.relationships = extract_relationships(connector)
        self.relationship_graph = build_relationship_graph(self.relationships)

    def get_tables(self) -> list[str]:
        """Return all table names in the schema."""
        if isinstance(self.raw_schema, dict):
            return list(self.raw_schema.keys())
        return []

    def get_columns(self, table_name: str) -> list[str]:
        """Return column names for a specific table."""
        if isinstance(self.raw_schema, dict):
            return self.raw_schema.get(table_name, [])
        return []

    def get_tables_for_column(self, column_name: str) -> list[str]:
        """Return all tables containing a column."""
        tables = []
        if isinstance(self.raw_schema, dict):
            for table, cols in self.raw_schema.items():
                if column_name in cols:
                    tables.append(table)
        return tables

    def has_table(self, table_name: str) -> bool:
        return table_name in self.get_tables()

    def has_column(self, table_name: str, column_name: str) -> bool:
        return column_name in self.get_columns(table_name)
