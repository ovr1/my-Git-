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
            with open('str4.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
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
        elif (self.path == '/srt5'):
            img = Image.open('srt5.jpg')
            img.show()
        elif (self.path == '/str6'):
            img = Image.open('str6.jpg')
            img.show()
            # Картинки
        elif (self.path == '/title.png'):
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
        elif (self.path == '/utyb.png'):
            with open('utyb.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/mail.png'):
            with open('mail.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/odn.png'):
            with open('odn.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/tel.png'):
            with open('tel.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/vb.png'):
            with open('vb.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/wac.png'):
            with open('wac.png', 'rb') as f:
                self.wfile.write(f.read())
        elif (self.path == '/hand.png'):
            with open('hand.png', 'rb') as f:
                self.wfile.write(f.read())
        #elif (self.path == '/Massage'):
            #with open('Massage.html', 'r', encoding='UTF-8') as f:  # читаем текстовый файл
                #lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                #output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                #self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
        #elif (self.path == '/Massage'):
            #with open('Massage.html', 'r', encoding='UTF-8') as f:  # читаем текстовый файл
                #lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                #output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                #self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
                    # Титульная Стр.
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
            print(registracyi)
        # вот здесь по-хорошему insert в базу надо взять в try-except на тот случай если произойдет ошибка
        # и ответить клиенту что операция на сервере произошла с ошибкой
        insert = MyHTTPRequestHandler.connection.prepare('''INSERT INTO public.postgres (id, first_namr, last_name, midle_name, age, v_purpose, tel, mail, passport)
                                                            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9);''')
        id = MyHTTPRequestHandler.connection.prepare('select nextval(\'postgres_id_seq\')')()[0][0] # готовим и сразу выполняем select по sequence который в результате нам вернет новый id
        insert(registracyi[0], registracyi[1], registracyi[2], registracyi[3], registracyi[4], registracyi[5], registracyi[6], registracyi[7], registracyi[8], registracyi[9])
        self._set_response() # готовим ответ
        self.wfile.write("Registracyi {} is added!<br><a href='/form'>Go back to registracyi.html".format(''.join(registracyi)).encode('utf-8')) # отвечаем клиенту что новый студент добавлен и даем ему ссылку на обратный переход на форму добавления

'''
Функция которая запускает сервер
'''
def run():
    db = None
    try:
        connection_string = 'pq://postgres:G24O02d24230303@127.0.0.1:5432/postgres'
        # создаем соединение с базой данной my_db по адресу хост 127.0.0.1, порт 5432, логин postgres, пароль 123456s
        db = postgresql.open(connection_string)
        exist = db.prepare("SELECT COUNT(*) FROM pg_class WHERE relname = 'postgres_id_seq'")()[0][0] # проверяем в системных каталогах есть ли наша последовательность для студентов
        if exist == 0: # если нет, то...
            db.execute("CREATE SEQUENCE postgres_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 10000000000 START 1 CACHE 1") # создаем ее
    except Exception:
        logging.error('Cann\'t connect to database with url {}'.format(connection_string))
        exit(-1)
    # Создаем http сервер который работает по порту 8000 и обрабатывает http запросы с помощью собственного MyHTTPRequestHandler
    try:
        PORT = 8012
        server_address = ("", PORT)
        MyHTTPRequestHandler.connection = db
        with HTTPServer(server_address, MyHTTPRequestHandler) as httpd:
            logging.debug("serving at port", PORT)
            # судя по описанию метода - обрабатывает запрос и ждет следующий пока сервер не будет выключен
            httpd.serve_forever()
    except Exception as e:
        logging.error('Something wrong with your server, port is {} \n See explanation {}'.format(PORT, e))
        exit(-1)

# для самостоятельного запуска скрипта
if __name__ == '__main__':
    run()