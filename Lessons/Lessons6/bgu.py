class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def energy(self):
        return self.fats * 9 + (self.carbs + self.proteins) * 4.2


    def __add__(self,other):
        return other  + self.energy()




tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)

breakfast = apple + tvorog_9
print("NutritionInfo(breakfast) = ",breakfast,"ккал")