import json # serve para importar 
import os # verifica se o arquivo existe

BANCO_DADOS = 'alunos.json' # Armazena uma variável

def cadastrar(): # cria uma função chamado cadrastar que pode criar comandos a serem executados depois.
    print("\n--- Novo Cadastro ---") # O \n funciona para cortar uma linha, e o print para aparecer no terminal.
    
    if os.path.exists(BANCO_DADOS): #Verifica se o arquivo alunos.json existe 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Serve para quando estiver aberto o arquivo, acessar Banco de dados, adicionar ao final da lista, e o encoding serve para dizer que o texto está em portugues.
            alunos = json.load(f) # Ele armazena o conjunto de informações por conta do JSON, e armazena em uma variável.
    else: # Se o arquivo não existe vai para o else.
        alunos = [] # No else cria uma nova lista vazia.

    novo_aluno = { # Cria um dicionário que armazena os dados que estão sendo pedidos, e podem ser chamados de valor e chave.
        "nome": input("Nome: "), # O valor foi criado como "Nome" e a chave foi atribuido com o input, que está escrito "Nome: "
        "telefone": input("Telefone: "), # O valor foi criado como "Telefone", e o input foi para mostrar o "Telefone: "
        "turma": input("Turma: "), # O valor foi criado como "Turma", e o input foi para mostrar o "Turma: ".
        "idade": int(input("Idade: ")), # O valor foi criado como "Idade" e o input foi para mostrar a "Idade: " e por ser um int tem que ser um número inteiro. 
        "cpf": input("CPF: ") # O valor foi criado como "cpf" e o input foi para mostrar o "CPF: " e por ser um input normal pode por vários números.
    } # Para fechar a chave.
    
    alunos.append(novo_aluno) # Foi feita uma variável com .append que serve para adicionar algo ao final da lista, neste caso no final da lista novo_aluno.

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Serve para quando estiver aberto a variável Banco_dados, reescrever por cima por conta do 'W', e para identificar que é em portugues por conta do encoding, fora dos parenteses o AS serve para criar um apelido, que seria o F.
        json.dump(alunos, f, indent=4, ensure_ascii=False) # É usada para salvar um objeto python (Como uma lista ou dicionário), em um arquivo no formato JSON e preservando caracteres especiais. 
        
    print("Aluno cadastrado com sucesso!") # Print para mostrar no terminal o que está dentro das aspas.

def listar(): # cria uma função chamado listar que pode criar comandos a serem executados depois.
    print("\n--- Lista de Alunos ---") # Print para mostrar no terminal o que está dentro das aspas e \n serve para quebrar uma linha.
    
    if os.path.exists(BANCO_DADOS): # Serve para SE o alunos.json existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Open abre o arquivo para a leitura, acha a função banco_dados e o encoding='utf-8' serve para mostrar que o texto está em portugues.
            alunos = json.load(f) # Ele armazena os dados dentro do arquivo JSON e armazena em uma variavel que é alunos.
    else: # Caso o arquivo não existe, ele vai para o else.
        alunos = [] # Cria uma variável com o nome alunos e armazena em uma lista que está vazia.

    if not alunos: # Verifica se a lista de alunos está vazia ou não.
        print("Nenhum aluno cadastrado.") # # Print para mostrar no terminal o que está dentro das aspas.
        return # Interrompe a ação do código.

    for aluno in alunos: # Cria um laço de repetição que percorre cada aluno da lista.
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # Print para mostrar no terminal o que está dentro das aspas, com o f no começo dos parenteses para conseguir adicionar as variáveis necessárias dentro nos parenteses.

def atualizar(): # Cria uma função chamada atualizar que pode criar comando a serem executados depois.
    print("\n--- Atualizar Aluno ---") # Print para mostrar no terminal o que está dentro das aspas e \n para quebrar uma linha.
    if not os.path.exists(BANCO_DADOS):  # Serve para SE o alunos.json existe
        print("Nenhum aluno cadastrado no sistema.")  # Print para mostrar no terminal o que está dentro das aspas.
        return # Interrompe a ação do código.

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Open abre o arquivo para a leitura, acha a função banco_dados e o encoding='utf-8' serve para mostrar que o texto está em portugues, e o AS serve para criar uma espécie de apelido, que no caso é o f.
        alunos = json.load(f) # Ele armazena os dados dentro do arquivo JSON e armazena em uma variavel que é alunos.
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # Na variável cpf_busca, terá um int que só aceita respostas com numeros, terá um input que mostrará o que está dentro dos parenteses.
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu() # Chama a função