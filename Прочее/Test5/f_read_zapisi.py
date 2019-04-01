file_name = 'number.txt'
file_name1 = 'registration3.txt'
print("Ваши записи: \n")
S = []
with open(file_name1, 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        ds = eval(str(line[1:-2]))
        S.append(ds['Пациент'])
    n = [1,2,3,...,100]
    S = list(zip(n,S))

L = []
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        line = eval(str(line[1:-2]))
        l = [line['-Месяц-'], line['-Дата-'], line['-Время-'], line['-Место-']]
        L.append(l)
    for line in zip(S,L):
        for x in line:
            print(x)
        print('\n')




