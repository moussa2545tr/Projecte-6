class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)

rectangle1 = Rectangle(5, 3)
print("Àrea:", rectangle1.area())
print("Perímetre:", rectangle1.perimetre())
