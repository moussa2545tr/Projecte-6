class Empleat:
    def calcular_sou(self):
        return 0

class Fixe(Empleat):
    def calcular_sou(self):
        return 2000

class Autonom(Empleat):
    def calcular_sou(self):
        return 1500

def mostrar_sous(empleats):
    for e in empleats:
        print(e.calcular_sou())

mostrar_sous([Fixe(), Autonom(), Fixe()])