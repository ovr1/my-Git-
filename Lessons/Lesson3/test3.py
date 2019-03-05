cycles = ["утро", "день", "вечер", "ночь"]
i = 0
while i < len(cycles):
   print(cycles[i])
   i = i + 1
print('\n')

cycles = ["утро", "день", "вечер", "ночь"]
for i in range(len(cycles)):
   print(cycles[i])
print('\n')

for i in range(5):
    print(i)
print('\n')

for i in range(10, 15):
    print(i)
print('\n')

for i in range(20, 30, 3):
    print(i)
print("--Можно и в другую сторону:")
for i in range(10, 1, -3):
    print(i)