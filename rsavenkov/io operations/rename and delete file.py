import os

with open('new name.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир!')

os.rename('new name.txt', 'old name.txt')
os.remove('old name.txt')