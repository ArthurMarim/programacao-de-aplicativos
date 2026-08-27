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
    