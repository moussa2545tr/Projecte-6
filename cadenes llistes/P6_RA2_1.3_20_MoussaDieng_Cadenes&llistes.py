vowels = 'aeiouàèéíòóú'
frase = input("Introdueix paraules separades per espais: ")
paraules = frase.split()
comencen_vocal = [p for p in paraules if p[0].lower() in vowels]
print("Paraules que comencen per vocal:", comencen_vocal)
