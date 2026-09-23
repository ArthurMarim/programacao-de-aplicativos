dias_semana = 1,2,3,4,5,6,7
pergunta_dia = int(input("Digite o dia da semana (APENAS NUMEROS): "))
match pergunta_dia:
    case 1:
        print ("Domingo")
    case 2:
        print ("Segunda")
    case 3:
        print ("Terça")
    case 4:
        print ("Quarta")
    case 5:
        print ("Quinta")
    case 6:
        print ("Sexta")
    case 7:
        print ("Sabado")
    case _:
        print ("Dia inválido!!")