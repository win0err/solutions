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

statement += " ORDER BY %s ASC" % order_by 
cur.execute(statement)

while True:
    row = cur.fetchone()
    if row == None:
        break
    print(*row)

con.close()