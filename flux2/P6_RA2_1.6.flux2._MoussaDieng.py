a, b = 0, 1
print("Primers 10 termes de Fibonacci:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
