def es_parell(numero):
    return numero % 2 == 0

for i in [1, 2, 3, 4, 5, 6]:
    print(f"El número {i} és parell: {es_parell(i)}")