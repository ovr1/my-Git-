class KitchenUtensil:
    def heat_up(self):
        pass


class Pan(KitchenUtensil):
    def __init__(self, size):
        self.size = size

    def heat_up(self):
        print("Сковорода подогревается")
Pan(20)

class Saucepan(KitchenUtensil):
    def __init__(self, volume, height):
        self.volume = volume
        self.height = height
        self.diameter = (4*volume / (3.14*height))**(1/2)

    def heat_up(self):
        print("Кастрюля диаметром %d см нагревается" % 100*self.diameter)
Saucepan(3, 0.125)

###
utensils = [Pan(20), Saucepan(3, 0.125)]
for u in utensils:
    u.heat_up()