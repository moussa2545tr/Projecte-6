nom_fitxer = "auto.txt"

try:
    with open(nom_fitxer, "r") as f:
        print(f.read())
except FileNotFoundError:
    with open(nom_fitxer, "w") as f:
        f.write("Fitxer creat automàticament.\n")
    print("Fitxer no trobat. S'ha creat automàticament.")
