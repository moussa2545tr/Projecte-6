def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat

print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))