import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2

    def perimetre(self):
        return 2 * math.pi * self.radi

cercle1 = Cercle(4)
print("Àrea del cercle:", cercle1.area())
print("Perímetre del cercle:", cercle1.perimetre())
