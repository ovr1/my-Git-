import postgresql
from datetime import timedelta, datetime as dt

list_users = {'sergei': (2018, 8, 3), 'valentin87': (2018, 8, 4), 'igor99': (2018, 7, 1), 'anton4': (2018, 1, 10), 'vera2000': (2018, 4, 14), 'sunnyside': (2018, 2, 24), 'sarah.connor': (2018, 1, 2), 'andrey3': (2018, 4, 21), 'alexei22': (2018, 2, 17)}

def cr_and_1w_db_postgres():
    db = postgresql.open("pq://Oleg:0209@127.0.0.1:5432/Lessons")
    db.execute("CREATE TABLE IF NOT EXISTS users (id numeric PRIMARY KEY,username varchar(20), last_seen timestamp)")

    for username, last_seen in list_users.items():
        p = username, last_seen
        V = (list(p))
        with db.xact() as xact:
            TablRegict = db.query("SELECT id FROM users")
            N = str(int(len(TablRegict)) + 1)
            V.insert(0, N)
            L = tuple(V)
            t = L[2]
            tablReg = db.prepare("INSERT INTO users VALUES ($1, $2, $3)")
            raise_Reg = db.prepare("UPDATE users SET username = $2, last_seen = $3 WHERE id = $1")
            with db.xact():
                tablReg(N, str(L[1]), dt(year=t[0], month=t[1], day=t[2]))

cr_and_1w_db_postgres()