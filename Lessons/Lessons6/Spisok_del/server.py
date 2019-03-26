from bottle import route, run, view


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

@route("/static/styles:C:Users\Oleg\PycharmProjects\my-Git-\Lessons\Lessons6\Spisok_del\static")
def sent_statik(styles):
    return styles(styles, rout='static')


@route("/")
@view("index")
def index():
    tasks = [
        TodoItem("прочитать книгу"),
        TodoItem("учиться жонглировать 30 минут"),
        TodoItem("помыть посуду"),
        TodoItem("поесть"),
    ]
    return {"tasks": tasks}

run(host="localhost", port=8080)