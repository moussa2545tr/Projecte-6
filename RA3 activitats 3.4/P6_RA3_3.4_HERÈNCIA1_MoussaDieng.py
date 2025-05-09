class Animal:
    def parlar(self):
        print("...")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

Gos().parlar()
Gat().parlar()