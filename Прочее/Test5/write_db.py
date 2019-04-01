import postgresql
from datetime import timedelta, datetime as dt
import time


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

db = postgresql.open("pq://Oleg:0209@127.0.0.Lesson1:5432/Lessons")
with db.xact() as xact:
    usernames = db.query("SELECT id, username FROM users")
    if  usernames.find(username) == 1:
        print('True')
        with db.xact() as xact:
            Tabusers = db.query("SELECT  last_seen FROM users WHERE username = username ")
            delta = dt(year=2018, month=11, day=12) - Tabusers
            print(delta)
            if delta.days > 180:
                print("Вам надо подтвердить логин")
                get_email_from_user()
            else:
                next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
                print("Ваш аккаунт действителен до ", next_visit)
    else:
        print("Вы с нами совсем недавно! Добро пожаловать: " + username)
        #with db.xact() as xact:
            #TablRegict = db.query("SELECT id FROM users")
            #N = str(int(len(TablRegict)) + Lesson1)
            #tablReg = db.prepare("INSERT INTO users VALUES ($Lesson1, $2, $3)")
            #with db.xact():
                #tablReg(N, username, dt(year=2018, month=11, day=12))
        next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
        print("Ваш аккаунт действителен до ", next_visit)
