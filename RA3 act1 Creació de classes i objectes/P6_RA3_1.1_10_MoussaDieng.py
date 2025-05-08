class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return math.hypot(self.x - altre.x, self.y - altre.y)

punt1 = Punt(0, 0)
punt2 = Punt(3, 4)
print("Distància:", punt1.distancia(punt2))
