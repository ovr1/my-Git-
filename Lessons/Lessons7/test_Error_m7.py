from bottle import route, run

@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    res = {"result": 0, "error": None}
    if bottom == 0:
        res["error"] = f"Для входных данных {top} и {bottom} не получилось: {'error'}"
    else:
        res["result"] = top / bottom
    return res


run(host="localhost", port="8080")