codigo = int(input("Digite o código do pacote: "))
peso = float(input("Digite o peso do seu produto: "))
status = "entrega normal"

if peso <= 5.00 and codigo % 10 == 0:
    status = "entrega expressa"
    print = (f"Pacote {codigo} {status}")
elif peso > 50.00:
    status = "carga pesada"
    print = (f"Pacote {codigo} {status}")
else:
    print ("Nenhuma informação")
