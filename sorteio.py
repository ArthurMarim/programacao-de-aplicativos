ID = int(input("Qual o seu ID? "))
valor = int(input("Qual o valor? "))

if ID % 2 == 0 and valor >= 500:
    print(f"Parabéns, usuário {ID}! Você ganhou um cupom para sua compra de R$ {valor}")
else:
    print (f"Obrigado pela compra, usuário {ID}. Continue acompanhando nossas promoções!")
