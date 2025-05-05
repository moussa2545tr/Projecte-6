try:
    n = int(input("Introdueix un nombre enter: "))
    print(f"Taula de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
except ValueError:
    print("Error: has d’introduir un nombre enter.")
