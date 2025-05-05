frase = input("Introdueix una frase: ").lower()
vocals = "aeiouàèéíïòóúü"
compte = sum(1 for c in frase if c in vocals)
print(f"La frase conté {compte} vocals.")
