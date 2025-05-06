with open("nombres.txt", "w") as f:
    f.write("10\nabc\n30\n")

with open("nombres.txt", "r") as f:
    for linia in f:
        try:
            valor = int(linia.strip())
            print(f"Valor llegit: {valor}")
        except ValueError:
            print(f"Error: '{linia.strip()}' no és un enter vàlid.")
