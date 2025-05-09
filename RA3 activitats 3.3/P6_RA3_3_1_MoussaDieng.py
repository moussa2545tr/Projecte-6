class Impressora:
    def imprimir(self, text):
        print("Imprimint:", text)

class Factura:
    def __init__(self, impressora):
        self.impressora = impressora

    def generar_factura(self):
        self.impressora.imprimir("Factura generada")