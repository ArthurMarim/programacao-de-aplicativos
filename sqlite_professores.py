import sqlite3


def criar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS professores(
                        id_professores integer primary key autoincrement,
                        nome_professores text not null,
                        materia_professores text,
                        idade_professores integer,
                        cpf_professores text unique not null,
                        salario_professores real not null,
                        escola_professores text not null)''')

    nome_completo = input("Digite seu nome completo: ")

    materia = input("Digite a matéria que deseja: ")
    idade = input("Digite a sua idade: ")
    cpf = input("Digite seu CPF completo: ")
    salario = input("Digite seu salário: ")
    escola = input("Digite qual escola você da aula: ")

    comando_inserir = f'''INSERT INTO professores (nome_professores, materia_professores, idade_professores, cpf_professores, salario_professores, escola_professores)
                        VALUES ('{nome_completo}','{materia}','{idade}','{cpf}','{salario}','{escola}')'''
    cursor.execute (comando_inserir)
    conexao.commit()

def listar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    cursor.execute (''' SELECT * FROM professores''')
    todos_professores = cursor.fetchall()
    if not todos_professores:
        print ("Nenhum aluno encontrado.")
    else:
        for professor in todos_professores:
            print (f"ID: {professor[0]}, Nome: {professor[1]}, Matéria: {professor[2]}, Idade: {professor[3]}, CPF: {professor[4]}, Salário: {professor[5]},Escola: {professor[6]}")
    conexao.close()

def atualizar():
    conexao = sqlite3.connect ('escola_demonstracao.db')
    cursor = conexao.cursor()
    id_busca = int(input("Digite seu ID: "))
    cursor.execute (f'''SELECT * FROM professores WHERE
                    ID = {id_busca}''')
    professores = cursor.fetchone()
    if not professores:
        print("Professor não encontrado")
        conexao.close()
        return
    else:
        novo_nome = input("Digite o novo nome: ")
        nova_materia = input("Digite a nova matéria: ")
        nova_idade = input("Digite sua nova idade: ")
        novo_cpf = input("Digite seu CPF atualizado: ")
        novo_salario = input("Digite seu novo salário: ")
        nova_escola = input("Digite sua nova escola: ")
        comando = f'''UPDATE professores SET nome = '{novo_nome}', materia = '{nova_materia}', idade = '{nova_idade}',
                                                     cpf = '{novo_cpf}', salario = '{novo_salario}', escola = '{nova_escola}'
                                                     WHERE id = {id_busca}'''
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def excluir():
    conexao = sqlite3.connect ('escola_demonstracao.db')
    cursor = conexao.cursor()
    listar()
    id_professores = int(input("Digite seu ID: "))
    cursor.execute (f'''DELETE FROM professores WHERE
                    id = {id_professores})''')
    conexao.commit()
    conexao.close()

def menu():
    while True:
        print ("~~OPÇÕES~~")
        print ("~~1- CRIAR USUÁRIOS~~")
        print ("~~2- LISTAR USUÁRIOS~~")
        print ("~~3- ATUALIZAR USUÁRIOS~~")
        print ("~~4- EXCLUIR USUÁRIO~~")
        print ("~~5- SAIR~~")

        opcao = input("Digite a opção que deseja selecionar: ")
        if opcao =="1":
            criar()
        elif opcao =="2":
            listar()
        elif opcao =="3":
            atualizar()
        elif opcao =="4":
            excluir()
        elif opcao =="5":
            return
        else:
            print("Digite uma opção válida")           
menu()
