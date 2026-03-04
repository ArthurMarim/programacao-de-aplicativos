cargo =str(input("Qual seu cargo? "))
codigo =int(input("Digite o código de acesso "))
escolha =input("Botão de emergencia S/N ")
protecao = input("Equipamento de proteção completo S/N ")

if (cargo == "Engenheiro" or cargo == "Tecnico") and (codigo == 1234 or escolha == "s") and protecao == "s":
    print ("Acesso liberado")
else:
    print ("Acesso negado")
