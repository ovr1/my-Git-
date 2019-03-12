from bottle import route, run, view
from datetime import datetime as dt
@route('/')
@view ("predictions")
def index():
    now = dt.now()
    return {"date": f"{now.year}-{now.month}-{now.day}"}

@route("/api/test")
def api_test():
    return {
        "test_passed": True
    }


run(
    host="localhost",
    port=8080,
    )