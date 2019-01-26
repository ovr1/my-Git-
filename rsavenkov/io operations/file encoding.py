import sys

print('Кодировка по умолчанию:', sys.getdefaultencoding())

print('-------------- Стих в кодировки UTF-8 --------------')
file_name_utf8 = 'стих utf8.txt'
f_utf8 = open(file_name_utf8, encoding='utf-8')
print(f_utf8.read())
f_utf8.close()

print('-------------- Стих в кодировки ANSI --------------')
file_name_cp1251 = 'стих ansi.txt'
f_cp1251 = open(file_name_cp1251, encoding='Cp1251')
print(f_cp1251.read())
f_cp1251.close()
