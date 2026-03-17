import sqlite3
from connectors.base_connector import BaseConnector

class SQLiteConnector(BaseConnector):
    def __init__(self, db_path):
        self.db_path = db_path

    def get_schema(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            columns = cursor.fetchall()
            schema[table_name] = [column[1] for column in columns]
        conn.close()
        return schema

    def execute_query(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results