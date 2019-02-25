def do_POST(self):
    content_length = int(self.headers['Content-Length'])  # определяем размер входящего сообщения
    post_data = self.rfile.read(content_length)  # читаем это сообщение
    registracyi = []
    data = str(post_data).split('&')  # обрабатываем данные от запроса
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
            raise_Reg(y[0], str(y[1]), str(y[2]), str(y[3]), y[4], str(y[5]), str(y[6]), str(y[7]), str(y[8]))
    self._set_response()  # готовим ответ
    self.wfile.write("Registracyi {} is added!<br><a href='/Registracyi'>Go back to registracyi.html".format(
        ''.join(registracyi)).encode(
        'utf-8'))  # отвечаем клиенту что новый студент добавлен и даем ему ссылку на обратный переход на форму добавления