def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n >= 2:
        print("Nombres primers:")
        for i in range(2, n + 1):
            if es_primer(i):
                print(i, end=" ")
    else:
        print("Introdueix un nombre enter major o igual que 2.")
except ValueError:
    print("Error: has d’introduir un nombre enter.")
