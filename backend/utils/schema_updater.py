def build_column_mapping(schema: dict) -> str:
    mapping = []

    for table, cols in schema.items():
        for col in cols:
            mapping.append(f"{col} -> {table}")

    return "\n".join(mapping)

def format_schema(schema: dict) -> str:
    formatted = ""

    for table, cols in schema.items():
        formatted += f"\nTable: {table}\nColumns: {', '.join(cols)}\n"

    return formatted