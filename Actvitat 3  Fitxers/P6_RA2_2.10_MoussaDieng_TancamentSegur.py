try:
    f = open("dades_segures.txt", "r")
    contingut = f.read()
    print(contingut)
finally:
    print("Tancant fitxer...")
    f.close()
