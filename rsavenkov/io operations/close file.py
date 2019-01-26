file_name = 'стих utf8.txt'

f = open(file_name)
f.close()

try:
    f = open(file_name)
finally:
    f.close()

with open(file_name, encoding='UTF-8') as f:
    print(f.read())