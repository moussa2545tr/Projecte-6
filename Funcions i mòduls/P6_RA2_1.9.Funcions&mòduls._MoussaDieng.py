def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "Encara és jove"
    elif edat < 65:
        estat = "Adult"
        descripcio = "En edat laboral"
    else:
        estat = "Jubilat"
        descripcio = "En etapa de descans"
    return estat, descripcio

for edat in [12, 25, 70]:
    estat, desc = estat_persona(edat)
    print(f"Edat {edat}: {estat} - {desc}")
