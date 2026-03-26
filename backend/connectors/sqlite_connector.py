import sqlite3
from connectors.base_connector import BaseConnector

class SQLiteConnector(BaseConnector):
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.text_factory = lambda b: b.decode("utf-8", errors="replace") if isinstance(b, (bytes, bytearray)) else b
        return conn

    def get_schema(self):
        conn = self._connect()
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
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results