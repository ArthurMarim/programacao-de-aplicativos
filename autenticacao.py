usuario = input("Qual o nome do usuario?")
senha = int(input("Qual a senha?"))

if (usuario == "admin" or usuario == "root") and senha == 1234:
    print ("Acesso liberado")
else:
    print ("Acesso negado")
