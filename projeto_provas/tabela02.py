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