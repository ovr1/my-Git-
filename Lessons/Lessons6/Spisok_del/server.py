import os
from bottle import route, run, view
from bottle import static_file


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

@route('/static/<filename>')
def sent_static(filename):
    return static_file(filename, root='./static/')


cwd = os.getcwd() + os.sep + "view" + os.sep + "index.tpl"
@route("/")
@view(cwd)
def index():
    tasks = [
        TodoItem("прочитать книгу"),
        TodoItem("учиться жонглировать 30 минут"),
        TodoItem("помыть посуду"),
        TodoItem("поесть"),
    ]
    return {"tasks": tasks}


run(host="localhost", port=8087)