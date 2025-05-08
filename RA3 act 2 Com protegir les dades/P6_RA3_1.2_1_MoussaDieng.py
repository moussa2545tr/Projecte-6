class CompteBancari:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  

    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat

    def retirar(self, quantitat):
        if quantitat > 0 and quantitat <= self.__saldo:
            self.__saldo -= quantitat
        else:
            print("Saldo insuficient")

    def consultar_saldo(self):
        return self.__saldo