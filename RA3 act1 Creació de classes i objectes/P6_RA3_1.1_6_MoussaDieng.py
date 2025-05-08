class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Saldo insuficient")

    def veure_saldo(self):
        return self.saldo

compte1 = CompteBancari(100)
compte1.ingressar(50)
compte1.retirar(30)
print("Saldo actual:", compte1.veure_saldo())
