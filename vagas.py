vagas = ["Livre", "Ocupado", "Livre", "Ocupado"]
indice = int(input("Digite uma vaga de 0 a 3: "))
if indice >= 0 and indice <= 3:
    if indice % 2 == 0 and vagas[indice] == "Livre":
        print (f"Vaga {indice} autorizada para estacionar ")
else:
    print(f"Vagas {indice} indisponiveis")
