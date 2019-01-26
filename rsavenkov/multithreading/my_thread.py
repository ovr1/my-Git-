# импортим библиотеку _thread унаследованную из Python 2. Она спроектирована в виде функций, старый стиль.
# нижнее подчеркивание говорит о том что библиотеку не рекомендуют к использованию,
# так как в будущих версия от нее могут отказаться, полностью убрав из Python
from _thread import start_new_thread

# счетчик потоков для этого примера
threadId = 1

# доработать программу следующим образом:
# 1. Добавить 3-ий поток который вычисляет факториал
# 2. Один из потоков бросает исключение при выполнении

'''
Функция вычисляющая факториал 5! = 1 * 2 * 3 * 4 * 5 = 120
Каждому потоку, который вычисляет факториал, присваивается отдельный threadId 
'''
def factorial(n):
    # global-ом говорим что значение переменной threadId используется контекстом выше - скрипта
    global threadId
    if n < 1:
        print("%s: %d" % ("Thread", threadId))
        threadId += 1
        return 1
    else:
        returnNumber = n * factorial(n - 1)
        print(str(n) + ' ! = ' + str(returnNumber))
        return returnNumber

# запускаем новый поток из скрипта, который тоже запущем в отдельном потоке - родительском. Передаем функцию factorial на выполнение потоку с параметров 5
start_new_thread(factorial, (5,))
# запускаем новый поток из скрипта, который тоже запущем в отдельном потоке - родительском. Передаем функцию factorial на выполнение потоку с параметров 4
start_new_thread(factorial, (4,))
# запускаем новый поток из скрипта, который тоже запущем в отдельном потоке - родительском. Передаем функцию factorial на выполнение потоку с параметров 3
start_new_thread(factorial, (3,))

# здесь родительский поток останавливается и ждет ввода с клавиатура. Чтобы показать что потоки которые он породил ранее уже закончили считать факториал и завершились
c = input("Waiting for threads to return.../n")
