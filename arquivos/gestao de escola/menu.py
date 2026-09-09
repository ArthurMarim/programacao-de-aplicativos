def menu_escola():
    try:
        while True:
            print("=====MENU====")
            print("1- Cadastrar Escola")
            print("2- Listar Escola")
            print("5- Cadastrar Turma")
            print("6- Listar Escola")
            print("7- Cadastrar Aluno")
            print("8- Listar Alunos")
            print("0- SAIR")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                cadastrar_escolas()
            elif opcao == "2":
                listar_escolas()
            elif opcao == "3":
                turmas_escola()
            elif opcao == "4":
                listar_turmas()
            elif opcao == "5":
                nome_alunos()
            elif opcao == "6":
                listar_alunos()
            elif opcao == "0":
                print("Programa Encerrado")
                break
            else:
                print("Opção Inválida!")
menu()