import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

def generate_prophecies(total_num=5, num_sentence=3):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentence):
            t = random.choise(times)
            a = random.choise(advices)
            p = random.choise(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentence - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)
    return prophecies

generate_prophecies(total_num=5, num_sentence=3)
global prophecies
print(prophecies)