class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya 

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            print("Contrasenya canviada")
        else:
            print("Contrasenya massa curta")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau