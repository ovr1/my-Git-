from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_predictions

@route("/")
@view("predictions2")
def index():
  now = dt.now()
  predictions = generate_predictions()
  x = random()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": f"{generate_predictions()}",
  }
()

@route("/api/test")
def api_test():
    return {"test_passed": True}

run(
  host="localhost",
  port=8080,
  autoreload=True
)