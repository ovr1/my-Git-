def make_header(word="Заголовок", tag="h1"):
    return "<%s>%s:</%s>" % (tag, word.capitalize(), tag)


print(make_header("важное сообщение"))
h1 = make_header
print(h1("внимательно"))

def make_header(word="Заголовок", tag="h1"):
    def f():
        return "<%s>%s:</%s>" % (tag, word.capitalize(), tag)
    return f()

print(make_header("важное сообщение"))

def make_tag_f(tag="h1"):
    def f(word):
        return "<%s>%s:</%s>" % (tag, word.capitalize(), tag)
    return f

h3 = make_tag_f(tag="h3")
print(h3("внимательно"))
print("\n")

def call_twice(f):
    f()
    f()

def print_thing_up():
    print("thing".upper())

call_twice(print_thing_up)
print("\n")

def my_decorator(my_f):
    def wrapper():
        print("Я внутри wrapper")
        my_f()
        print("Я уже вызвал твою функцию, но ещё внутри wrapper")

    return wrapper

def some_function():
    print("Притворимся, что я тут что-то полезное делаю")

some_function()
print("-----")
decorated = my_decorator(some_function)
print("*****")
decorated()
print("-----")

def my_decorator(my_f):
    def wrapper():
        print("Я внутри wrapper")
        my_f()
        print("Я уже вызвал твою функцию, но еще внутри wrapper")

    return wrapper

@my_decorator
def some_function():
    print("Притворимся, что я тут что-то полезное делаю")

some_function()