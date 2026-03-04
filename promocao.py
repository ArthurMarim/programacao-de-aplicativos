valor = float(input("Digite o seu valor da compra "))
prime = input("Voce é assinante prime (s/n)")

if valor >= 50.0 or prime == "s" and valor < 100:
    frete = 0
else:
    frete = 50
    print ("Frete de 50 reais adicionado")
total = valor + frete

print ("Valor da compra foi de ", total)