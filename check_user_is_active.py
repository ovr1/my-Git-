from datetime import timedelta, datetime as dt
import time
file_name = 'list_users.txt'

list_users = {}

list_users['sergei'] = 2018,8,3
list_users['valentin87'] = 2018,8,4
list_users['igor99'] = 2018,7,1
list_users['anton4'] = 2018,1,10
list_users['vera2000'] = 2018,4,14
list_users['sunnyside'] = 2018,2,24
list_users['sarah.connor'] = 2018,1,2
list_users['andrey3'] = 2018,4,21
list_users['alexei22'] = 2018,2,17
print(list_users)


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


if username not in list_users:
    print("Вы с нами совсем недавно! Добро пожаловать: " + username)
    list_users[username] = 2018, 11, 12
    with open(file_name , 'a', encoding="utf-8") as f:
        f.write(str(list_users) + '\n')
    with open(file_name, 'r', encoding='utf-8') as f:
        list_users = f.readlines()
        print(list_users)
else:

    L = list_users[username]
    delta = dt(year=2018, month=11, day=12) - dt(year=L[0], month=L[1], day=L[2])
    if delta.days > 180:
        print("Вам надо подтвердить логин")
        get_email_from_user()
    else:
        next_visit = dt(year=2018, month=11, day=12) + timedelta(days=180)
        print("Ваш аккаунт действителен до ", next_visit)



