class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores 

    def set_hores(self, noves_hores):
        if 0 <= noves_hores <= 23:
            self.__hores = noves_hores
        else:
            print("Hores fora de rang")

    def get_hores(self):
        return self.__hores

    def mostrar_hores(self):
        return f"{self.__hores:02d}:00"