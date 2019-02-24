# импортируем стандартный веб сервер и обработчик запросов
from http.server import BaseHTTPRequestHandler, HTTPServer
# импортим библиотеку для логирования, удобно логировать входящие запросы в случае с веб серверами
import logging
# импортим в код библиотеку postgresql для работы с базой данных postgresql
import postgresql
from PIL import Image


'''
Исходя из названия, обработчик http запросов. Необходим нам при создании http сервера
Определяет два метода которые будут обрабатывать get и post запросы, в которых мы напишем свою логику обработки запросов
Наследуем от BaseHTTPRequestHandler иначе ничего работать не будет!
'''

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    # Аттрибут класса нашего обработчика который запоминает соединение с базой
    # Необходим будет при обработке post запроса сразу записывать данные в базу
    connection = None

    '''
    Вспомогательный метод который устанавликает код ответа и заголовок Content-type
    '''
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    '''
    Переопределяем от родителя метод который обрабатывает все get запросы к серверу
    '''
    def do_GET(self):
        self._set_response()
                #Запросы:
        if (self.path == '/form'):  # если uri содержит /form
            with open('registraciy.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines() # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines) # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8')) # пишем нашу строку в сеть запросившему клиенту
        elif (self.path == '/zapis'):
            with open('zapis.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
        elif (self.path == '/cont'):
            with open('Contact.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
                    # Стр. 2,3,4
        elif (self.path == '/str2'):
            with open('str.2.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
        elif (self.path == '/str3'):
            with open('str.3.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
        elif (self.path == '/str4'):
            with open('str.4.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
                # Стр. Massage
        elif (self.path == '/Massage'):
            with open('Massage.html', 'r', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
                    # Стрю 5,6
                # Картинки
        elif (self.path == '/image.png'):
            with open('title.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/foto1.jpg'):
            with open('foto1.jpg', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/foto2.jpg'):
            with open('foto2.jpg', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/foto3.jpg'):
            with open('foto3.jpg', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/log.png'):
            with open('utyb.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/log1.png'):
            with open('mail.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/log2.png'):
            with open('odn.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/log3.png'):
            with open('tel.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/log4.png'):
            with open('vb.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/log5.png'):
            with open('wac.png', 'rb') as f:
                self.wfile.write(f.read())

        elif (self.path == '/hand.png'):
            with open('hand.png', 'rb') as f:
                self.wfile.write(f.read())

        elif (self.path == '/srt5'):
            img = Image.open('srt5.jpg')
            img.show()
        elif (self.path == '/str6'):
            img = Image.open('str6.jpg')
            img.show()
        else: # случай когда uri запроса отличный от /form, на этот случай обработки не предусмотрено
            with open('base.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
    '''
    Переопределяем от родителя метод который обрабатывает все post запросы к серверу
    '''

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # определяем размер входящего сообщения
        post_data = self.rfile.read(content_length) # читаем это сообщение
        registracyi = []
        data = str(post_data).split('&') # обрабатываем данные от запроса
        for d in data:
            logging.info(d.split('=')[1])
            registracyi.append(d.split('=')[1])
        y = registracyi[:]
        print(y)
        id = MyHTTPRequestHandler.connection.prepare('select nextval(\'postgres\public\Galy_id_seq\')')()[0][
            0]  # готовим и сразу выполняем select по sequence который в результате нам вернет новый id
        insert = MyHTTPRequestHandler.connection.prepare('''INSERT INTO registracyi(id, first_name,last_name, midle_name, age, v_purpose, tel, mail, passport)  
                                                                            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)''')
        raise_Reg = insert.prepare(
            "UPDATE registracyi SET first_name = $2, last_name = $3, midle_name = $4, age = $5, v_purpose = $6, tel = $7, mail = $8, passport = $9 WHERE id = $1")
        with insert.xact() as xact:
            TablRegict = insert.query("SELECT id FROM registracyi")
            N = str(int(len(TablRegict)) + 1)
            y.insert(0, N)
            with insert.xact():
                raise_Reg(y[0], str(y[1]), str(y[2]), str(y[3]), y[4], str(y[5]),  str(y[6]), str(y[7]), str(y[8]))
        self._set_response()  # готовим ответ
        self.wfile.write( "Registracyi {} is added!<br><a href='/Registracyi'>Go back to registracyi.html".format(
                        ''.join(registracyi)).encode(
                        'utf-8'))  # отвечаем клиенту что новый студент добавлен и даем ему ссылку на обратный переход на форму добавления

'''
Функция которая запускает сервер
'''
def run():
    db = None
    insert = postgresql.open("pq://postgres:0306@127.0.0.1:5432/Galy")
    insert.execute("CREATE TABLE IF NOT EXISTS registracyi(id numeric PRIMARY KEY,first_name text,last_name text, midle_name text, age numeric,v_purpose varchar(20), tel numeric, mail varchar(20), pasport varchar(20))")
    # создаем соединение с базой данной Galy по адресу хост 127.0.0.1, порт 5432, логин postgres, пароль 0306
    # Создаем http сервер который работает по порту 8000 и обрабатывает http запросы с помощью собственного MyHTTPRequestHandler
    try:
        PORT = 8015
        server_address = ("", PORT)
        MyHTTPRequestHandler.connection = insert
        with HTTPServer(server_address, MyHTTPRequestHandler) as httpd:
            logging.debug("serving at port", PORT)
            # судя по описанию метода - обрабатывает запрос и ждет следующий пока сервер не будет выключен
            httpd.serve_forever()
    except Exception as e:
        logging.error('Something wrong with your server, port is {} \n See explanation {}'.format(db, e))
        exit(-1)

    # для самостоятельного запуска скрипта
    if __name__ == '__main__':
        run()