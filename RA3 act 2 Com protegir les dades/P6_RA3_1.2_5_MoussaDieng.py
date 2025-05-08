class Sensor:
    def __init__(self, valor=0):
        self._valor = valor 

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self._valor = nou_valor
        else:
            print("Valor fora de rang")
