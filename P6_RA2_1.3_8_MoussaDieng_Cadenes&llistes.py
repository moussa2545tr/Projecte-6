def elimina_espais(cadena):
    return cadena.replace(" ", "")

text = input("Escriu una cadena: ")
print("Sense espais:", elimina_espais(text))
