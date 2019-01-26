# импортим библиотеку, ссылка на сайт https://pythonhosted.org/py-postgresql/
# изучите ее api
import postgresql

# создаем и получаем соединение с базой данных
# формат строки соединения такой:
#
#    pq://                      <пользователь>                          :               <пароль>        @               <хост>                  :                       <порт>                  /<база данных>
#     ^                                ^                                ^                   ^           ^                  ^                    ^                          ^                        ^
#     |                                |                                |                   |           |                  |                    |                          |                        |
#  обязательный префик          пользователь на подключаемой      разделить пары         пароль      разделитель       ip адресс машины где   раздедитель пары          порт по которому        имя базы данных
#   задаваемый этой либой               базе                        user:password                       пар            запущен сервер бд        host:port               работает сервер бд
db = postgresql.open("pq://my_user:123456@localhost:5432/my_db")
# готовим через объект соединение select в базу по табличке student. Выбираем все поля
my_select = db.prepare("SELECT * FROM frame")

# открывает транзакцию. Кстати, можно спокойно работать без этой строчки!
with db.xact():
    # открываем файл на запись
    with open('C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/db/data.txt', 'w', encoding='utf-8') as f:
        # перебираем в цикле строчки полученные через select
        for row in my_select:
            # каждую строчку пишем в файл
            f.writelines(str(row) + '\n')

# that's all folks