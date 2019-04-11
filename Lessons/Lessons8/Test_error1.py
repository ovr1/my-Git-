d = {"answer": 42}
def f(k):
    try:
        value = d[k]
    except KeyError:
        value = 0
    return value

print(d["answer"])
print(d["question"])