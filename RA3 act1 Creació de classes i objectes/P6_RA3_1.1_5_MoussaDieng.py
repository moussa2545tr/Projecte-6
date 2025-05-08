class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5

estudiant1 = Estudiant("Joan", 6.5)
print("Ha aprovat:", estudiant1.ha_aprovat())