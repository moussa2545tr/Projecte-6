from P6_RA3_7_MoussaDieng import Cercle

cercles = [Cercle(2), Cercle(5), Cercle(10)]

for c in cercles:
    if c.area() > 50:
        print(f"Cercle amb radi {c.radi} té àrea {c.area():.2f}")
