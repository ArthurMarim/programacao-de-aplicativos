estado = input("Digite a sigla do estado (PR, RS ou SC): ")
match estado:
    case "PR":
        print ("Paraná")
    case "RS":
        print ("Rio Grande do Sul")
    case "SC"
        print ("Santa Catarina")
    case _:
        print ("Você está fora da região sul")
    