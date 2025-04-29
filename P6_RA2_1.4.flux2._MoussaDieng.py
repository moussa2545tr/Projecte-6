import random

secret = random.randint(1, 100)
print("He pensat un número entre l'1 i el 100. Endevina'l!")

while True:
    guess = int(input("El teu número: "))
    if guess < secret:
        print("Massa baix!")
    elif guess > secret:
        print("Massa alt!")
    else:
        print("Enhorabona, ho has encertat!")
        break
