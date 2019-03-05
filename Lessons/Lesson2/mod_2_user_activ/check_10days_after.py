all_months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
def num_days(year, month):
    need_change_to_30 = (month>6 and not(month %2)) or (month <=6 and (month % 2))
    num_days = 31
    if month == 1:
        if year % 4 == 0:
            num_days = 29
        else:
            num_days = 28
    elif need_change_to_30:
        num_days = 30
    global N
    N = int(num_days)
    print(N)


def  check_10days_after(month, date):
    delta = day_of_visit+10
    global D
    D = int(delta)

year_of_visit = int(input("Введите год Вашего визита-  "))
montt_of_visit = int(input("Введите порядковый номер месяцы вашего последнего посещения-  ")) -1
day_of_visit = int(input("Введите день вашего последнего посещения-  "))

num_days(year_of_visit, montt_of_visit)
check_10days_after(montt_of_visit, day_of_visit)

if N >= D:
    print("True")
else:
    print("False")
