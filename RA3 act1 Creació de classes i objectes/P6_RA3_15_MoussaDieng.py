from P6_RA3_4_MoussaDieng import Producte

def aplicar_descompte(productes):
    for p in productes:
        p.aplicar_descompte(10)
        print(f"{p.nom} - nou preu: {p.preu:.2f}€")

llista = [
    Producte("Ordinador", 800),
    Producte("Ratolí", 20)
]

aplicar_descompte(llista)
