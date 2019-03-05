def num_days(month):
    all_months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
                  'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    need_change_to_30 = (month>6 and not(month %2)) or (month <=6 and (month % 2))
    num_days = 31
    if month == 1:
        num_days = 28
    elif need_change_to_30:
        num_days = 30
    N = print(num_days)

num_days(11)