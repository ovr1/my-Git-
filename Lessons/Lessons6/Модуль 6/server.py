from bottle import route, run, static_file, view, redirect, request
from db import TodoItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
s = Session()

#class TodoItem:
#   def __init__(self, description, unique_id):
#       self.description = description
#       self.is_completed = False
#       self.uid = unique_id

#   def __str__(self):
#       return self.description.lower()

#tasks_db = {
#   1: TodoItem("прочитать книгу",1),
#   2: TodoItem("учиться жонглировать 30 минут", 2),
#   3: TodoItem("помыть посуду", 3),
#   4: TodoItem("поесть", 4),
#}
 
@route("/static/<filename>")
def send_static(filename):
    return static_file(filename, root="static")

cwd = os.getcwd() + os.sep + "view" + os.sep + "index.tpl"
@route("/")
@view(cwd)
def index():
    tasks = s.query(TodoItem).order_by(TodoItem.uid)
    return {"tasks": tasks}

@route("/add-task", method="POST")
def add_task():
    desc = request.POST.description.strip()
    if len(desc) > 0:
        t = TodoItem(desc)
        s.add(t)
        s.commit()
    return redirect("/")


@route("/api/delete/<uid:int>")
def api_delete(uid):
    s.query(TodoItem).filter(TodoItem.uid == uid).delete()
    s.commit()
    return redirect("/")

@route("/api/complete/<uid:int>")
def api_complete(uid):
    t = s.query(TodoItem).filter(TodoItem.uid == uid).delete()
    t.is_completed = True
    s.commit()
    return "Ok"


###
run(host="localhost", port=8085, autoreload=True)
