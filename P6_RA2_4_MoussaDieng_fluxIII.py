try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n >= 0:
        for i in range(0, n + 1, 2):
            print(i, end=" ")
    else:
        print("Error: el nombre ha de ser positiu o zero.")
except ValueError:
    print("Error: has d’introduir un nombre enter.")
