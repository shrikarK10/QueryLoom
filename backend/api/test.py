import sqlite3
conn = sqlite3.connect(r"backend\api\Chinook_Sqlite.sqlite")
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()
print(tables)