file_name = 'стих utf8.txt'

f = open(file_name, 'r+')
print('File attributes:')
print('closed:', f.closed)
print('mode:', f.mode)
print('name:', f.name)