from bottle import route, run
from datetime import datetime as dt
from random import random

import random
now = dt.now()

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

@route("/generate")
def generate():
    predictions = generate_predictions()
    print(predictions[0])
    return {
        "date": f"{now.year}-{now.month}-{now.day}",
	    "p-0" : "predictions[0]",
	    "p-1" : "predictions[1]",
	    "p-2" : "predictions[2]",
	    "p-3" : "predictions[3]",
	    "p-4" : "predictions[4]",
	    "p-5" : "predictions[5]",
        }
run(
  host="localhost",
  port=8080,
  autoreload=True
    )