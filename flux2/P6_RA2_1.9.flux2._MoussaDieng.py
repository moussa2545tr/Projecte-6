nums = list(map(float, input("Introdueix una llista de números (separats per espais): ").split()))
if nums:
    print("El número màxim és:", max(nums))
else:
    print("Llista buida.")
