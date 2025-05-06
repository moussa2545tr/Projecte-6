with open("missatge.txt", "w") as f:
    f.write("Aquest és el missatge dins el fitxer.")

with open("missatge.txt", "r") as f:
    contingut = f.read()
    print(contingut)
