file_name = 'стих utf8.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    print('----- первые 100 символов ------')
    print(f.read(100))
    print('------ следующие за ними 10 символов ------')
    print(f.read(10))
    print('------- весь файл до конца ----')
    print(f.read())
    print('------- пусто ----')
    print(f.read())
    print('-----------')