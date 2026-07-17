import sqlite3
conn = sqlite3.connect(r"Chinook_Sqlite.sqlite")
c = conn.cursor()
c.execute("""SELECT Track.Name ,SUM(InvoiceLine.Quantity) as S
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.Name
ORDER BY S DESC
LIMIT 1;""")
tables = c.fetchall()
print(tables)