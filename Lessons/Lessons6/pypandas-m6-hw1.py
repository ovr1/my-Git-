from datetime import datetime as dt
import sqlite3 as lite
import sys

S = []
L = []
N = []

con = lite.connect('access_log.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM main.logs[access_log]")
    rows = cur.fetchall()
    for row in rows[1:]:
        if "109.234.35.42"  in row:
            S.append(row)

print("S = ",len(S))
print("N = ", len(rows))

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM main.logs[access_log] WHERE TIMESTAMP LIKE '2018-09-01%'")
    rows = cur.fetchall()
    for row in rows[1:]:
        L.append(row)
l = print("L = ",len(L))

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM main.logs[access_log] WHERE TIMESTAMP LIKE '2018-09-10%'")
    rows = cur.fetchall()
    for row in rows[1:]:
        N.append(row)
n = print("N = ",len(N))

print(7304-6696)