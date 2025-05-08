class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Cotxe: {self.marca} {self.model} ({self.any})")

cotxe1 = Cotxe("Toyota", "Corolla", 2020)
cotxe1.mostrar_info()