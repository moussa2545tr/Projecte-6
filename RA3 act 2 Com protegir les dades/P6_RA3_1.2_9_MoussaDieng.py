class Joc:
    def __init__(self):
        self.__puntuacio = 0  

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0

    def get_puntuacio(self):
        return self.__puntuacio