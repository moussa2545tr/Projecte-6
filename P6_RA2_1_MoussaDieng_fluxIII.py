try:
    n = int(input("Introdueix un número enter: "))
    for i in range(n + 1):
        print(i, end=" ")
except ValueError:
    print("Error: has d’introduir un nombre enter.")
