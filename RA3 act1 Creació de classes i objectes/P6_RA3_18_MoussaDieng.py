from P6_RA3_9_MoussaDieng import Llibre

class Biblioteca:
    def __init__(self):
        self.llibreta = []

    def afegir_llibre(self, llibre):
        self.llibreta.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibreta:
            llibre.mostrar_info()

biblio = Biblioteca()
biblio.afegir_llibre(Llibre("1984", "George Orwell", 1949))
biblio.afegir_llibre(Llibre("El Petit Príncep", "Antoine de Saint-Exupéry", 1943))
biblio.mostrar_llibres()
