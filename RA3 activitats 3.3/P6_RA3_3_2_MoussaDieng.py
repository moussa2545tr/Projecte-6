class NotificadorEmail:
    def enviar(self, missatge):
        print("Enviant per email:", missatge)

class Comanda:
    def __init__(self, notificador):
        self.notificador = notificador

    def confirmar(self):
        self.notificador.enviar("La comanda ha estat confirmada")