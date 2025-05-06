import os

nom_fitxer = "dades.txt"

if os.path.exists(nom_fitxer):
    with open(nom_fitxer, "r") as f:
        print(f.read())
else:
    print(f"Error: El fitxer {nom_fitxer} no existeix.")
