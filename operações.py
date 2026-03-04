saldo = 1000.00 # variavel float
opcoes = input("Escolha entre Deposito, Saque ou Extrato ")

if opcoes == "Deposito":
    deposito = float(input("Digite a quantia que voce deseja depositar: "))
    if deposito > 0.00 :
        valor_total = saldo + deposito
        print ("Depósito efetuado, seu saldo atual é ", valor_total)
else:
    print ("Erro")

if opcoes == "Saque":
    saque = int(input("Qual o valor do saque? "))
    if saque > 0 and saque <= 1000.00 or 100.00:
        valor_total2 = saldo - saque
        print ("Seu saldo atual é de ", valor_total2)
else:
    print ("Erro")

if opcoes == "Extrato":
    print ("Seu extrato é de ", saldo)
else:
    print ("Erro")
    