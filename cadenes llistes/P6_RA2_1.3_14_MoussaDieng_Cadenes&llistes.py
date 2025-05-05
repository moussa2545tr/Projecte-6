parells = []
senars = []
for _ in range(10):
    num = int(input("Introdueix un número: "))
    if num % 2 == 0:
        parells.append(num)
    else:
        senars.append(num)
print("Parells:", parells)
print("Senars:", senars)
