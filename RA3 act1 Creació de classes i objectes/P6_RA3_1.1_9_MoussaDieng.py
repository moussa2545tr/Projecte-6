class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"'{self.titol}' de {self.autor} ({self.any})")

llibre1 = Llibre("1984", "George Orwell", 1949)
llibre1.mostrar_info()
