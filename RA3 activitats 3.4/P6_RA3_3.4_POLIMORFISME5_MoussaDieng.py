class Vehicle:
    def moure(self):
        pass

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe condueix per carretera")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta pedala pel carril bici")

class Barca(Vehicle):
    def moure(self):
        print("La barca navega pel mar")

def simular_moviment(vehicles):
    for v in vehicles:
        v.moure()

simular_moviment([Cotxe(), Bicicleta(), Barca()])