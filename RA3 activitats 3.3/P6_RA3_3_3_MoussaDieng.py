class Descompte20:
    def aplicar(self, total):
        return total * 0.8

class CarretCompra:
    def __init__(self, descompte):
        self.descompte = descompte
        self.productes = []

    def afegir_producte(self, preu):
        self.productes.append(preu)

    def total_final(self):
        total = sum(self.productes)
        return self.descompte.aplicar(total)