from bottle import route, run, view


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False


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
