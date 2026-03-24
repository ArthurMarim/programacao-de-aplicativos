lista = ["Alice","Bob","Carlos"]
autorizacao = input("Qual o nome do pesquisador? ")

if autorizacao in lista:
    indice = lista.index(lista)
    print (f"Acesso Permitido! O pesquisador {lista} está na posição {autorizacao}.")
    remover = (input("Deseja remover essa pessoa da lista? S/N"))
    
    if remover == "S":
        autorizacao.remove(autorizacao)
        print(f"lista atual {lista}")
    else:
        print ("Saindo do programa...")
else:
    print (f"Acesso Negado! O pesquisador {autorizacao} não foi encontrado.")
    add_pesquisador = input("Voce deseja adicionar esse pesquisador? S/N")
    if add_pesquisador == "S":
        print("O pesquisador foi atualizado.")
        print(f"Nova lista {lista}")
    else:
        print ("Nenhuma alteração foi feita")

