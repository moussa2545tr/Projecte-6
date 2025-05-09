class Figura:
    def dibuixar(self):
        print("Figura genèrica")

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle")

figures = [Cercle(), Quadrat(), Triangle()]
for f in figures:
    f.dibuixar()