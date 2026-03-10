garrafas = int(input("Qual o total de garrafas que passaram pela esteira hoje? "))

if garrafas == 500:
    print("HORA DA LIMPEZA: Parar maquina imediatamente")
    print("Qualidade: Retirar amostra para o teste ")


elif garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar maquina imediatamente")

elif garrafas % 100 == 0:
    print ("Qualidade: Retirar amostra para o teste ")

else:
    print(f"Produção em dia. Garrafa numéro {garrafas}")