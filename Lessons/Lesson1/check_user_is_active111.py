from datetime import timedelta, datetime as dt
import time
file_name = 'list_users.txt'

list_users = {}
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

with open(file_name, 'r', encoding='utf-8') as f:
    ds = f.readlines()
    ds = eval(str(ds[1:-1]))
    for line in ds:
        list_users = line
        print(list_users)
        for k, v in list_users.items():
            print(k, ':', v)
if username not in list_users:
    print("Вы с нами совсем недавно! Добро пожаловать: " + username)
    list_users[username] = 2018, 11, 12
    with open(file_name , 'a', encoding="utf-8") as f:
        f.write(str(list_users))
else:

    L = list_users[username]
    delta = dt(year=2018, month=11, day=12) - dt(year=L[0], month=L[1], day=L[2])
    if delta.days > 180:
        print("Вам надо подтвердить логин")
        get_email_from_user()
        print('Спасибо!')
        next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
        print("Ваш аккаунт действителен до ", next_visit)

    else:
        next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
        print("Ваш аккаунт действителен до ", next_visit)



