class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")

persona1 = Persona("Anna", 25)
persona1.presentar_se()
