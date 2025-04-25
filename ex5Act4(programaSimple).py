PI = 3.1416  # Constant

def area_cercle(radi):  # Funció
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))  # Entrada de l'usuari
print("L'àrea del cercle és:", area_cercle(radi))  # Sortida per pantalla

