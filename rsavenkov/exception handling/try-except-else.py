from math import pow

x = input('Ваше число будет возведено в степеь 2:')

try:
    x = int(x)
    print('В блоке try начало')
    print(int(pow(x, 2)))
    print('В блоке try конец')
    print(' ')
except TypeError:
    print('В блоке except', TypeError)
    x = int(x)
    print(pow(x, 2))    # обработать ValueError
except ValueError:
    print(' ')
    print('Введите число, не букву (Блок except (ValueError)')
else:
    print('Блок else, в том случае если исключение не вызвано') # необходимо попасть в этот блок