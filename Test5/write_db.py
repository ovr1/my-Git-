import postgresql
from datetime import timedelta, datetime as dt

db = postgresql.open("pq://Oleg:0209@127.0.0.1:5432/Lessons")
db.execute("CREATE TABLE IF NOT EXISTS users (id numeric PRIMARY KEY,username varchar(20), last_seen timestamp)")

tablReg = db.prepare("INSERT INTO users VALUES ($1, $2, $3)")
raise_Reg = db.prepare("UPDATE users SET username = $2, last_seen = $3 WHERE id = $1")

with db.xact():
    tablReg(2, 'valentin87', dt(2018, 8, 4))