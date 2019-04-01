file_name = 'registration3.txt'
file_name1 = 'number3.txt'
import pickle

print("Список пациентов: \n")
with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        ds = eval(str(line[1:-2]))
        for k, v in ds.items():
            print(v)
        print('\n')

with open(file_name, 'r', encoding="utf-8") as f:
    cont = f.readlines()
    Kol_pacientov: int = len(cont)


    with open('Kol_pacientov.pickle','wb') as f:
        pickle.dump(Kol_pacientov, f)

    with open('Kol_pacientov.pickle','rb') as f:
        print('Количество пациентов = ', Kol_pacientov)