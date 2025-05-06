try:
    with open("resultats.txt", "w") as f:
        f.write("Prova d'escriptura amb gestió d'errors.\n")
except PermissionError:
    print("Error: No tens permís per escriure en aquest fitxer.")
