media = float(input("Qual a sua media?"))
renda = float(input("Quantos é sua renda?"))
esc = input("Voce veio de escola publica? s/n")

if media >= 8.0 and renda < 2.000 or esc == "s":
    print ("Voce ganhou a bolsa")
else:
    print("Voce nao ganhou a bolsa")

    