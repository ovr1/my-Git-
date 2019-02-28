from datetime import timedelta, datetime as dt
from Lessons.db import query_user_last_seen
import time

from Lessons.db import list_users

registered_users = list_users()
i = 0
while i < len(registered_users):
    username = registered_users[i][0]
    last_seen = registered_users[i][1]
    print(i + 1, username, last_seen.date())
    i = i + 1

existing_username = list_users()[0][0]
last_seen = query_user_last_seen(existing_username)


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


if username is existing_username in registered_users:
    print("Вы с нами совсем недавно! Добро пожаловать: " + username)
else:
    delta = dt(year=2018, month=11, day=12) - query_user_last_seen(username)
    print(query_user_last_seen(username))
    if delta.days > 180:
        print("Вам надо подтвердить логин")
        get_email_from_user()
    else:
        next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
        print("Ваш аккаунт действителен до ", next_visit)
