frase = input("Escriu una frase: ")
vowels = "aeiouàèéíòóúü"
count = sum(1 for c in frase.lower() if c in vowels)
print("Nombre de vocals:", count)
