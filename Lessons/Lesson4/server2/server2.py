from bottle import route, run, view
from datetime import datetime as dt
from random import random

import random

times = ["утром", "днем", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_predictions(total_num=6, num_sentences=2):
    predictions = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        predictions.append(forecast)

    return predictions

@route("/")
@view("predictions2")
def index():
  now = dt.now()
  predictions = generate_predictions()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": f"{list(generate_predictions())}",
  }

@route("/api/test")
def api_test():
    return {"test_passed": True}

run(
  host="localhost",
  port=8080,
  autoreload=True
)