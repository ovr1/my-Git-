from bottle import route, run
from my_math import careful_division

import logging

logger = logging.getLogger("divider")
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s -- %(name)s::%(levelname)s %(message)s"
)
handler = logging.FileHandler("my_app.log")
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


def danger(top, bottom):
    return {
        "result": careful_division(top, bottom),
        "error": None,
    }


if __name__ == "__main__":
    for x in range(1, 5, 2):
        for y in range(-4, 2, 4):
            if y == 0 or x == 0:
                logger.info("Кто-то пытается делить на ноль!")
            print(danger(x, y))