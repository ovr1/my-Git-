from bottle import route, run, view

@route('/')
view ("predictions")
def index():
    return {"date":}

@route("/api/test")
def api_test():
    return {
        "test_passed": True
    }


run(
    host="localhost",
    port=8080,
    )