nome_cliente = str(input("Digite seu nome: "))
valor_compra = float(input("Digite o valor total da compra: "))
entrega = float(input("Qual a distancia em quilometros? "))
cupom_especial = input ("Voce deseja colocar cupom especial? ") 
if cupom_especial == "S":
    print ("Seu cupom foi solicitado ")
elif cupom_especial == "N":
    print ("Seu cupom não será solicitado")
else:
    print ("Não entendi")

if valor_compra >= 1000.00 and cupom_especial == "S":
     print ("Seu cupom é VIP20")
elif valor_compra > 500 and valor_compra < 1000 and cupom_especial == "S":
    print ("Seu cupom é CUP10")

valor_total = input("Digite o cupom que apareceu: ")

if valor_total == "CUP10":
    desconto= valor_compra * 0.10
    total = valor_compra - desconto
elif valor_compra == "VIP20":
    desconto= valor_compra * 0.20
    total = valor_compra - desconto


if 
    
