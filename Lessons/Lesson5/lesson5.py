from pathlib import Path
file_name = "lesson5.txt"

n = int(len(set(Path(r'C:\Users\Lenovo\PycharmProjects\pyweb-m4-hw2\lesson5.txt').read_text(encoding='utf-8').split())))
print(n)

l = int(len(set(Path(r'C:\Users\Lenovo\PycharmProjects\pyweb-m4-hw2\lesson5.txt').read_text(encoding='utf-8').split('.'))))
print(l)
print(round(l/n*100),'%')
print(round((l/(n-l))*100),'%')

with open(file_name, 'r', encoding="UTF-8") as f:
    content = f.read()

    w = int(len(content.split()))
    print(w)
    t = int(len(content.split('.')))
    print(t)

    print(round(t/w *100), '%')