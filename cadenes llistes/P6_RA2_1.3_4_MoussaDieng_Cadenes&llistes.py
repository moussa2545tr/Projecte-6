paraula = input("Introdueix una paraula: ").lower()
if paraula == paraula[::-1]:
    print("És un palíndrom.")
else:
    print("No és un palíndrom.")
