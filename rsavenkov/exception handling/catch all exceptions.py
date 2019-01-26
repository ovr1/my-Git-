my_code = '''
def my_func(arg1, arg2):
    return arg1 / arg2

result = my_func(3, 4)
result = my_func(6, 0)
print(result)
'''

try:
    exec(my_code)   # Обработать IndentationError, ZeroDivisionError
# except:
#     print('Ошибка в коде')
except:
    print('--------->')