class Animal:
    def fer_soroll(self):
        return "..."

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())

reproduir_soroll(Gat())
reproduir_soroll(Vaca())