import postgresql
from datetime import timedelta, datetime as dt
import time

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
            global t
            t = L[2]
            tablReg = db.prepare("INSERT INTO users VALUES ($1, $2, $3)")
            raise_Reg = db.prepare("UPDATE users SET username = $2, last_seen = $3 WHERE id = $1")
            with db.xact():
                tablReg(N, str(L[1]), dt(year=t[0], month=t[1], day=t[2]))

cr_and_1w_db_postgres()

def get_email_from_user(attempts=3, sleep_duration=10):
    email = input("Введите e-mail: ")
    i = 1
    while (email.find("@") == -1):
        print("неправильный email. Попробуйте еще раз")
        i = i + 1
        email = input("Попытка " + str(i) + ". Введите e-mail: ")
        if i % attempts == 0:
            print("Переборщили с попытками. Подождите " + str(sleep_duration) + " секунд")
            time.sleep(sleep_duration)
    return email


def make_username(email):
    return email.split("@")[0].lower()


email = get_email_from_user()
username = make_username(email)

db = postgresql.open("pq://Oleg:0209@127.0.0.1:5432/Lessons")
with db.xact() as xact:
    Tabusers = db.query("SELECT username FROM users")
    if username not in Tabusers:
        print("Вы с нами совсем недавно! Добро пожаловать: " + username)

        with db.xact() as xact:
            TablRegict = db.query("SELECT id FROM users")
            N = str(int(len(TablRegict)) + 1)
            tablReg = db.prepare("INSERT INTO users VALUES ($1, $2, $3)")
            with db.xact():
                tablReg(N, username, dt(year=2018, month=11, day=12))
    else:
        with db.xact() as xact:
            Tabusers = db.query("SELECT username, last_seen FROM users")
            print(Tabusers)
            delta = dt(year=2018, month=11, day=12) - dt(year=t[0], month=t[1], day=t[2])
            if delta.days > 180:
                print("Вам надо подтвердить логин")
                get_email_from_user()
            else:
                next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
                print("Ваш аккаунт действителен до ", next_visit)
