import os

class QuitProgramException(Exception):
    '''
    Моя ошибка которая описывает пользовательски выход из программы
    '''
    def __init__(self):
        self.message = 'Сеанс ввода завершен. Посмотрите содержимое файла {}'

disk_letters = ['A', 'B', 'C', 'D']

print('Добро пожаловать в консольную программу записи файла! Для выхода из нее введите команду quit()')

def checkIsWinCorrectPath(file):
    '''
    Проверяет корректность пути в nt системах
    :param file:
    :return:
    '''
    if (file is None or file == ''):
        print('Введенное значение "{}" не является файлом!'.format(file))
        return -1

    if (file[0] not in disk_letters) or (file[1:3] != ':\\'):
        print('Введенное значение "{}" не является файлом!'.format(file))
        return -1

    dirs = file.split('\\')[1:-1]

    path = ''
    for dir in dirs:
        path = path + '\\' + dir
        if not os.path.isdir(file[0:3] + path):
            print('Введенное значение "{}" не является файлом!'.format(file))
            return -1

    return 0

if __name__ == '__main__':

    file = input('Введите имя файла:')
    error_code = checkIsWinCorrectPath(file)

    if error_code != 0:
        exit(error_code)

    with open(file, 'w', encoding='utf-8') as f:
        try:
            first = input('Введите содержимое файла:')
            f.writelines(first + '\n')
            while True:
                line = input()
                if line == 'quit()':
                    #exit(0)
                    raise QuitProgramException()
                f.writelines(line + '\n')
        except QuitProgramException as e:
            print(e.message.format(f.name))
            error_code = 0
        except KeyboardInterrupt as e:
            print('\nНепредвиденное завершение программы! Фалй не создан!')
            error_code = 2

    if error_code != 0:
        os.remove(file)

    exit(error_code)

