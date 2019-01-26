# библиотека для создания новых процессов, не путать с потоками!
import subprocess

# вызывает процесс notepad.exe в системе, дожидаясь его завершения
code = subprocess.call("notepad.exe")
# code = subprocess.call(["notepad.exe", "C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/multithreading/my_subprocess.py"])
# печатает код возврата вызванного процесса
print('return code:', code)

# тоже самое что и call(), только не дожидается конца выполнения процесса
args = ["ping", "www.yahoo.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)