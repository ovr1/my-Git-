import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

n = 0
while n <3:
    n+=1
    print("\n",n,"-предсказание")

    y = []
    i = 0
    while i < 4:
        i += 1

        index1 = random.randrange(0,len(times))
        time = times[index1].capitalize()

        index2 = random.randrange(0, len(advices))
        advice = advices[index2]

        index3 = random.randrange(0, len(promises))
        promise = promises[index3]

        y.append(time + ' ' + advice + ' ' + promise + '.')

    for a in y:
        print(a)