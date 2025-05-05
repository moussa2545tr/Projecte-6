try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n > 0:
        print("La suma és:", sum(range(1, n + 1)))
    else:
        print("Error: has d’introduir un enter positiu.")
except ValueError:
    print("Error: has d’introduir un nombre enter.")
