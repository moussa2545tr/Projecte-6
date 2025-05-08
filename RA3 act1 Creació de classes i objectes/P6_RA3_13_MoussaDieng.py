from P6_RA3_5_MoussaDieng import Estudiant

estudiants = [
    Estudiant("Anna", 7),
    Estudiant("Marc", 4),
    Estudiant("Júlia", 9)
]

for est in estudiants:
    if est.ha_aprovat():
        print(f"{est.nom} ha aprovat amb un {est.nota}")
