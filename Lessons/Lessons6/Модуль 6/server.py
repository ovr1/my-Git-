from bottle import route, run, static_file, view, redirect, request
from db import TodoItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
s = Session()


@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


cwd = os.getcwd() + os.sep + "view" + os.sep + "index.tpl"
@route("/")
@view(cwd)
def index():
    tasks = s.query(TodoItem).order_by(TodoItem.uid)
    total_tasks = s.query(TodoItem).count()
    return {"tasks": tasks,
            "total_tasks": total_tasks,
            }


@route("/add-task", method="POST")
def add_task():
    desc = request.POST.description.strip()
    if len(desc) > 0:
        t = TodoItem(desc)
        s.add(t)
    incomplete = s.query(TodoItem).filter(TodoItem.is_completed == False).count()
    if incomplete <=10:
        s.commit()
        return redirect("/")
    else:
        return {"total_tasks": "Too much tasks, not executed!!!"}

@route("/api/delete/<uid:int>")
def api_delete(uid):
    s.query(TodoItem).filter(TodoItem.uid == uid).delete()
    s.commit()
    return redirect("/")


@route("/api/complete/<uid:int>")
def api_complete(uid):
    t = s.query(TodoItem).filter(TodoItem.uid == uid).first()
    t.is_completed = True
    s.commit()
    return "Ok"

###
run(host="localhost", port=8080)