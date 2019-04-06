# coding: utf-8
from bottle import request, route, run
from my_logging import get_logger

logger = get_logger("divider-server")

@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    res = {"result": 0, "error": None}
    try:
        res["result"] = top / bottom
    except ZeroDivisionError as error:
        res["error"] = f"Для входных данных {top} и {bottom} не получилось: {error}"
        agent = request.headers["User-Agent"]
        host = request.headers["Host"]
        path = request.path
        logger.error(f"Ошибка деления при обращении к {host}{path}. User-Agent: {agent}")

    return res

if __name__ == "__main__":
    run(host="localhost", port=8080)