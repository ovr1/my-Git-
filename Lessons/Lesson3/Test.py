s = """Я хитрая многострочная строка
меня не остановят ваши жалкие переносы
мвахаха
"""
print(s)
print('\n')

s = "Я хитрая многострочная строка\nменя не остановят ваши жалкие переносы\nмвахаха"
print(s)
print('\n')

header = "Основное предсказание"
forecast = "На днях будет четверг. На днях был четверг."
paragraph = "<h1>%s</h1><p>%s</p>" % (header, forecast)
print(paragraph)

print('\n')

header = "Основное предсказание"
paragraph = "<{tag}>{content}</{tag}>".format(tag="h1", content=header)
paragraph = "<{0}>{1}<{0}>".format("h1", header)
print(paragraph)

print('\n')
p = "%.3f" % 3.1415926 #можно записать как
p2 = "{0:.3f}".format(3.1451926)
print(p,p2)
print('\n')
day = 'день'
night = 'ночь'
uran_sightings = '{0} {1} {0} {1} {1} {1} {0} {0} {1}'.format(day, night)
print(uran_sightings)