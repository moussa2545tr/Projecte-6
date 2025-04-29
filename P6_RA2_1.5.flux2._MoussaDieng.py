n = int(input("Introdueix un nombre enter positiu: "))

if n < 2:
    print(f"{n} no és primer.")
else:
    és_primer = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            és_primer = False
            break
    if és_primer:
        print(f"{n} és un nombre primer.")
    else:
        print(f"{n} NO és un nombre primer.")
