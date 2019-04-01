a = 123456789
b = 0
try:
    print(a / b)
except Exception:
    print("На ноль делить нельзя!")

try:
   fp = open("non-existent.txt", "r")
except Exception:
   print("Файл не найден, ничего не будет")
else:
   print("Файл найден, продолжаю!")


def danger(N, i, start=0):
    return range(start, N)[i]

def caution(x, y):
    z = 0
    try:
        z = danger(x, y)
    except IndexError as e:
        print(e)
    return z

print(caution(10, 5))
print(caution(10, 20))

#def danger(N, i, start=0):
#    return range(start, N)[i]

#def caution(x, y):
#    z = danger(x, y)
#    return z

#print(caution(10, 5))
#print(caution(10, 20))





















