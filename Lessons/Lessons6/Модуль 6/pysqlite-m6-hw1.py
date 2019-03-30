from datetime import datetime as dt
import sqlite3 as lite
import sys

S = []
L = []


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
    cur.execute("SELECT * FROM main.logs[access_log] WHERE TIMESTAMP > '2018-09-01 00:00:00.000000'AND TIMESTAMP < '2018-09-10 00:00:00.000000'")
    rows = cur.fetchall()
    for row in rows:
        L.append(row)
print("L = ",len(L))

fd = {}
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM main.logs[access_log]")
    rows = cur.fetchall()
    for row in rows:
        ip = row[1]
        if ip in fd:
            n = fd[ip]
            fd[ip] = fd[ip] + 1
        else:
            fd[ip] = 1
for k,v in fd.items():
    if int(v) > 2850:
        print(v,k)


l = (73875 + 17970 + 9878)/710424*100