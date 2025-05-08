class Alumne:
    def __init__(self, edat):
        self.__edat = edat  

    def set_edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
        else:
            print("Edat no vàlida")

    def get_edat(self):
        return self.__edat