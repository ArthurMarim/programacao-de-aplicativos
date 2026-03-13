cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Preto"]
escolha = int(input("Digite um numero entre 1 a 5"))

if 1 <= escolha <= 5:
    print ("A cor escolhida é",cores[escolha - 1 ])
else:
    print ("Numero invalido!")
    