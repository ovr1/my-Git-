file_name = '1.txt'

with open(file_name, 'a', encoding="utf-8") as f:
    f.write('Это первая строка которую я записал в файл из программы\n')
    f.write('Это вторая строка которую я записал в файл из программы\n')
    f.write('Конец\n')

with open(file_name, 'r', encoding='utf-8') as f:
    content = f.readlines()
    # content = f.read()

for line in content:
    print(line)
