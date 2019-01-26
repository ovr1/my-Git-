def func(arg1, arg2):
    print(arg1, arg2)

try:
    func(1,2)
    #func1(2)
except (ValueError, TypeError):
    print('----------->')