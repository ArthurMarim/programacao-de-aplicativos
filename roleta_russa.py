senha = input("Digite sua senha:")
tentativas = int(input("Digite quantas tentativas voce tentou: "))
token = (" Possui token (s/n) ")

if senha == "admin123" and (tentativas % 3 == 0) or token == "s":
    print (f"tentativa N{tentativas}, acesso permitido")
else:
    print (f"tentativa N {tentativas}, acesso negado")
