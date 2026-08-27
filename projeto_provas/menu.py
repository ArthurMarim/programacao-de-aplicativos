from tabela01 import operadoras, listar_operadoras, atualizar_operadora, excluir_operadora
from tabela02 import agencias, listar_agencias, atualizar_agencia, excluir_agencia

def menu():
    while True:
        print("=====MENU====")
        print("1- Cadastrar Operadora")
        print("2- Listar Operadora")
        print("3- Atualizar Operadora")
        print("4- Deletar Operadora")
        print("5- Cadastrar Agencia")
        print("6- Listar Agencia")
        print("7- Atualizar Agencia")
        print("8- Deletar Agencia")
        print("0- SAIR")
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            operadoras()
        elif opcao == "2":
            listar_operadoras()
        elif opcao == "3":
            atualizar_operadora()
        elif opcao == "4":
            excluir_operadora()
        elif opcao == "5":
            agencias()
        elif opcao == "6":
            listar_agencias()
        elif opcao == "7":
            atualizar_agencia()
        elif opcao == "8":
            excluir_agencia()
        elif opcao == "0":
            print("Programa Encerrado")
            break
        else:
            print("Opção Inválida!")
menu()