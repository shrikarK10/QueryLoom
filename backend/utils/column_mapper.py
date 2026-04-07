def build_column_to_table_map(schema: dict):
    column_to_table = {}

    for table, columns in schema.items():
        for col in columns:
            if col not in column_to_table:
                column_to_table[col] = []
            column_to_table[col].append(table)

    return column_to_table