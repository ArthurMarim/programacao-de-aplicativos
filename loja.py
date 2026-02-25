valor_total = float(input("Qual o valor da sua compra? "))
cupom = input("digite o cupom ")


desconto = valor_total * 0.10 
novo_preco = valor_total - desconto
 

if cupom == "DEV10":
    print ("Seu cupom foi aplicado!", novo_preco)
else:
    print("CUPOM INVALIDO")

