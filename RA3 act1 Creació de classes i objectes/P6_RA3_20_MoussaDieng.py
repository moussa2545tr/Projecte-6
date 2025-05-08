from P6_RA3_3_MoussaDieng import Persona

def mostrar_grans(persones):
    for p in persones:
        if p.edat > 30:
            print(f"{p.nom}, {p.edat} anys")

llista = [
    Persona("Laura", 25),
    Persona("Joan", 35),
    Persona("Carla", 40)
]

mostrar_grans(llista)
