with open("sortida.txt", "r+") as f:
    contingut = f.read()
    print("Contingut original:")
    print(contingut)
    f.write("Línia afegida en mode r+.\n")
