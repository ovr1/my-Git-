# raise MemoryError('Ошибка памяти')

print('Мой собственный интерпретатор Питон! Поехали!')

while(True):
    i = input('>>>')
    if i == 'quit()':
        break
    try:
        result = eval(i)
        print(result)
    except:
        raise Exception('Синтаксическая ошибка! Недопустимый оператор!', i)