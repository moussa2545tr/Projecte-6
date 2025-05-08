from P6_RA3_6_MoussaDieng import CompteBancari

compte = CompteBancari(100)

compte.ingressar(50)
compte.retirar(30)
compte.retirar(150)  # superior al saldo

compte.veure_saldo()
