# def menu():
#     while true:
#         print("1. Cadastrar aluno")
#         print("2. Sair")
#         opcao = input("Escolha: ")

#         if opcao == "1":
#             print("Cadastrando... ")
#         elif opcao == "2":
#             print("Saindo do Programa.")
# # Por que o programa continua rodando e mostrando o menu mesmo selecionando a opção 2?
#             pass

# # Mesmo se a opção for "2" pois não interrompe o laço, tem que usar um break para sair do while.

def menu():
    while True:
        print("1. Cadastrar aluno")
        print("2. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")
        elif opcao == "2":
            print("Saindo do Programa.")
            break
        else:
            print("Opção inválida.")