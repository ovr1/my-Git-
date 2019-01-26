import os

print(os.getcwd())
os.chdir('C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov')
os.system('mkdir newDir')

import os

print(dir(os))
help(os)

import shutil

with open('src.txt', 'w', encoding='utf-8') as src:
    src.write('Data in source file')
with open('target.txt', 'w', encoding='utf-8') as target:
    pass

shutil.copyfile('src.txt', 'target.txt')
shutil.move('target.txt', 'newDir/target.txt')