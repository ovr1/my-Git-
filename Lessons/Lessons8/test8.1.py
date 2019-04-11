def h1_result(f):
    def wrapper():
        res = f()
        return "<h1>" + res + ":</h1>"
    return wrapper

@h1_result
def my_function():
    return "Следите за руками"

print(my_function())
print("\n")

import random
class File():
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
        files = []
        for _ in range(10000):
            with File('my_file.txt') as outfile:
                outfile.write(str(random.randint()))