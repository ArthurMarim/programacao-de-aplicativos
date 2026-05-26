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
    
    for aluno in alunos: # Cria um laço de repetição que percorre cada aluno da lista.
        if aluno['cpf'] == cpf_busca: # Serve para se a variável Aluno for cpf e ser igual a variável cpf_busca, apareca a linha de baixo
            print(f"Editando dados de: {aluno['nome']}") # Se a linha de cima for verdadeira, aparece essa linha
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # pedir um novo nome ao usuário. Se ele digitar algo, o nome é atualizado Se apenas pressionar Enter, o nome antigo é mantido.
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] # Solicita um novo telefone caso nada seja digitado, o telefone atual continua o mesmo.
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # pede uma nova turma para o aluno se o campo ficar vazio, a turma antiga permanece.
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) # solicita uma nova idade. O valor digitado é convertido para número inteiro com int(). Se o usuário não digitar nada, a idade atual é mantida.
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] # pede um novo CPF. Se o usuário apenas pressionar Enter, o CPF antigo continua armazenado.
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Open abre o arquivo para a reescrever por cima, acha a função banco_dados e o encoding='utf-8' serve para mostrar que o texto está em portugues, e o AS serve para criar uma espécie de apelido, que no caso é o f.
                json.dump(alunos, f, indent=4, ensure_ascii=False) # Json.dump guarda a lista de alunos e salva no arquivo f
            print("Dados atualizados com sucesso!") # Print para mostrar o que está entre parenteses e aspas se o nome nao estiver cadastrado
            return # Interrompe a ação do código.
            
    print("Aluno não encontrado.") # Print para mostrar o que está entre parenteses e aspas 

def excluir(): # Cria uma função chamada atualizar que pode criar comando a serem executados depois.
    print("\n--- Excluir Aluno ---") # Print para mostrar o que está entre parenteses e aspas 

    if not os.path.exists(BANCO_DADOS): # Serve para SE o alunos.json não existir mostrar a linha de baixo.
        print("Nenhum aluno cadastrado no sistema.") # Se a linha de cima for verdadeira, aparecerá esse print.
        return # Interrompe a ação do código.

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # Open abre o arquivo para leitura, acha a função banco_dados e o encoding='utf-8' serve para mostrar que o texto está em portugues, e o AS serve para criar uma espécie de apelido, que no caso é o f.
        alunos = json.load(f) # # Ele armazena os dados dentro do arquivo JSON e armazena em uma variavel que é alunos.
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # Na variável id_busca, terá um int que só aceita respostas com numeros, terá um input que mostrará o que está dentro dos parenteses.
    
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # 
    
    if len(nova_lista) < len(alunos): # Json.dump guarda a lista de alunos e salva no ar quivo F no formato json
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # Open abre o arquivo para leitura, acha a função banco_dados e o encoding='utf-8' serve para mostrar que o texto está em portugues, e o AS serve para criar uma espécie de apelido, que no caso é o f.
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!") # Print para mostrar o que está entre parenteses e aspas 

    else: # Caso o IF não de certo vai para o else
        print("Aluno não encontrado.") # Print para mostrar o que está entre parenteses e aspas 


def menu(): # Cria uma função chamada atualizar que pode criar comando a serem executados depois.
    if not os.path.exists(BANCO_DADOS): # Serve para SE o alunos.json não existir mostrar a linha de baixo.
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # Open abre o arquivo para a reescrever por cima, acha a função banco_dados e o encoding='utf-8' serve para mostrar que o texto está em portugues, e o AS serve para criar uma espécie de apelido, que no caso é o f.
            json.dump([], f)  # Json.dump guarda a lista de alunos e salva no arquivo f

    while True: # Enquanto for verdadeiro mostrará os prints abaixo
        print("\n=== SISTEMA ESCOLAR ===") # Print para mostrar o que está entre parenteses e aspas e \n para quebrar a linha 

        print("1. Cadastrar Aluno") # Print para mostrar o que está entre parenteses e aspas 

        print("2. Listar Alunos") # Print para mostrar o que está entre parenteses e aspas 

        print("3. Atualizar Aluno") # Print para mostrar o que está entre parenteses e aspas 

        print("4. Excluir Aluno") # Print para mostrar o que está entre parenteses e aspas 

        print("5. Sair") # Print para mostrar o que está entre parenteses e aspas 

        
        opcao = input("Escolha uma opção: ") # Variável com um input na frente para mostrar o que está dentro das aspas
        
        if opcao == '1': cadastrar() # Se a variavel opcao for igual a 1 ira para cadastrar
        elif opcao == '2': listar() # Caso a variavel opcao for igual a 2 aparecerá listar
        elif opcao == '3': atualizar() # Caso a variavel opcao for igual a 3 aparecerá listar
        elif opcao == '4': excluir() # Caso a variavel opcao for igual a 4 aparecerá excluir
        elif opcao == '5': break # Caso a variavel opcao for igual a 5 irá acabar o código
        else: print("Opção inválida!") # Caso não seja nenhuma das opções anteriores aparecerá esse print com o que está dentro das aspas.

menu() # Chama a função