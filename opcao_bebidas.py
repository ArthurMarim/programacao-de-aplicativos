print ("1- Café")
print ("2- Chá")
print ("3- Suco")

opcao = int(input("Digite qual opção: "))
match opcao:
    case 1:
        print("Café")
    case 2:
        print("Chá")
    case 3:
        print("Suco")
    case 4:
        print ("Essa opção não existe!")
    