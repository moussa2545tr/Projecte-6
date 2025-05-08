class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        self.preu -= self.preu * (percentatge / 100)

producte1 = Producte("Portàtil", 1000)
producte1.aplicar_descompte(10)
print(f"Preu amb descompte: {producte1.preu}€")
