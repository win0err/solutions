import sqlite3
import sys

db = input()

con = sqlite3.connect(db)
cur = con.cursor()

conditions = [line for line in sys.stdin]
order_by = conditions.pop()

statement = "SELECT condition FROM Talks"
if len(conditions) > 0:
    statement += " WHERE " + " AND ".join(conditions)

statement += f" ORDER BY {order_by} ASC"
cur.execute(statement)

for row in cur.fetchall():
    print(*row)

con.close()
