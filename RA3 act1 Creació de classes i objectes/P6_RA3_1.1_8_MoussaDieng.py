class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("fa un soroll")

animal1 = Animal("Rex", "gos")
animal1.fer_soroll()