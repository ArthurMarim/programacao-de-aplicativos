import sqlite3

def operadoras():
    try:
        conexao = sqlite3.connect('agencia_viagens.db')
        cursor = conexao.cursor()
        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS operadoras (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_empresa TEXT NOT NULL,
                            registro_turismo TEXT UNIQUE NOT NULL
                            )
                            '''
                        )
        nome_empresa = input("Digite o nome da sua empresa: ")
        registro_turismo = input("Digite o REGISTRO DE TURISMO (ex: 123456): ")

        comando_inserir = '''INSERT INTO operadoras (nome_empresa , registro_turismo)
                                VALUES (?,?)'''
                            
        cursor.execute (comando_inserir, (nome_empresa , registro_turismo))
        id_operadora = cursor.lastrowid
        conexao.commit()
    
        print ("Operadora cadastrada com sucesso!")
        print (f"ID da operadora {id_operadora}")

    except sqlite3.IntegrityError:
        print("ERRO: Esse registro de turismo já está cadastrado")
    finally:
        conexao.close()


def listar_operadoras():
    conexao = sqlite3.connect('agencia_viagens.db')
    cursor = conexao.execute('''
                            SELECT * FROM operadoras
                            '''
                            )       
    todos_operadores = cursor.fetchall()
    if not todos_operadores:
        print("Nennhum operador encontrado")
    else:
        for operadora in todos_operadores:
            print(f"ID: {operadora[0]}, Empresa: {operadora[1]}, Registro: {operadora[2]} ") 
    conexao.close()

def atualizar_operadora():
    conexao = sqlite3.connect ('agencia_viagens.db')
    cursor = conexao.cursor()
    id_operadora = int(input("Digite o ID da operadora que você deseja atualizar: "))
    cursor.execute ('''SELECT * FROM operadoras WHERE id = ? ''', (id_operadora,))
    operadora = cursor.fetchone()

    if not operadora:
        print ("Operadora não encontrada!")
        conexao.close()
        return

    else:
        novo_nome = input("Digite o novo nome da empresa: ")
        novo_registro_turismo = input("Digite o novo Registro de Turismo: ")

    cursor.execute(
    '''UPDATE operadoras
       SET nome_empresa = ?, registro_turismo = ?
       WHERE id = ?''', (novo_nome, novo_registro_turismo, id_operadora))

    conexao.commit()
    print ("Operadora atualizada com sucesso!")
    conexao.close()
                    
def excluir_operadora():
    conexao = sqlite3.connect ('agencia_viagens.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    listar_operadoras()
    id_operadora = int(input("Digite qual o ID da operadora que deseja excluir: "))
    cursor.execute (f'''DELETE FROM operadoras WHERE id = ?''', (id_operadora,))
    conexao.commit()
    conexao.close()
    print("Operadora excluida com sucesso!")
    

def agencias():
    try:
        conexao = sqlite3.connect('agencia_viagens.db')
        cursor = conexao.cursor()
        cursor.execute ('''PRAGMA foreign_keys = ON''')
        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS agencias (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            localizacao_agencia TEXT NOT NULL,
                            id_operadora INTEGER NOT NULL,
                            FOREIGN KEY (id_operadora) REFERENCES operadoras(id)
                            )
                            '''
                        )
        localizacao_agencia = input("Digite a localização da agencia: ")
        id_operadora = int(input("Digite o ID da operadora: "))

        comando_inserir = f''' INSERT INTO agencias (localizacao_agencia , id_operadora)
                                VALUES (?,?)'''
        cursor.execute (comando_inserir, (localizacao_agencia, id_operadora))
        conexao.commit()
        print ("Agencia Cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("ERRO: Essa agencia não existe!")
    finally:
        conexao.close()

def listar_agencias():
    conexao = sqlite3.connect('agencia_viagens.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT * FROM agencias
    ''')
    todas_agencias = cursor.fetchall()
    if not todas_agencias:
        print("Nenhuma agencia encontrada")
    else:
        for agencia in todas_agencias:
            print(
                f"ID: {agencia[0]}, Localização: {agencia[1]}, ID Operadora: {agencia[2]}")
    conexao.close()

def atualizar_agencia():
    conexao = sqlite3.connect('agencia_viagens.db')
    cursor = conexao.cursor()
    cursor.execute('''PRAGMA foreign_keys = ON''')

    id_agencia = int(
        input("Digite o ID da agencia que você deseja atualizar: "))
    cursor.execute(
        '''SELECT * FROM agencias WHERE id = ?''',(id_agencia,))
    agencia = cursor.fetchone()
    if not agencia:
        print("Agencia não encontrada!")
        conexao.close()
        return
    else:
        nova_localizacao = input("Digite a nova localização da agencia: ")

        novo_id_operadora = int(input("Digite o novo ID da operadora: "))
    cursor.execute(
        '''UPDATE agencias
           SET localizacao_agencia = ?, id_operadora = ?
           WHERE id = ?''',
        (nova_localizacao, novo_id_operadora, id_agencia))
    conexao.commit()
    print("Agencia atualizada com sucesso!")
    conexao.close()

def excluir_agencia():
    conexao = sqlite3.connect('agencia_viagens.db')
    cursor = conexao.cursor()
    cursor.execute('''PRAGMA foreign_keys = ON''')
    listar_agencias()
    id_agencia = int(input("Digite qual o ID da agencia que deseja excluir: "))
    cursor.execute(
        '''DELETE FROM agencias WHERE id = ?''',(id_agencia,))
    conexao.commit()
    conexao.close()
    print("Agencia excluída com sucesso!")

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