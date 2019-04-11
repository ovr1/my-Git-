#d = {"answer": 42}
#def f(k):
#   return d[k]

#print(f("answer"))
#print(f("question"))
#print("\n")

#d = {"answer": 42}
#def f(k):
#    if k in d:
#        return d[k]
#    else:
#        return 0

#print(d["answer"])
#print(d["question"])

#d = {"answer": 42}
#def f(k):
#    try:
#        value = d[k]
#    except KeyError:
#        value = 0
#    return value

#print(d["answer"])
#print(d["question"])

from collections import defaultdict

def default():
    return 0

data = [2, 4, 7, 7, 8, 9, 2, 10]
d = defaultdict(default)

for el in data:
    d[el] += 1

print("Элементы в данных, которые встречаются больше одного раза:")
for k in d:
    if d[k] >= 2:
        print("'%s' (встречается %s раз)" % (k, d[k]))