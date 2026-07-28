# import sqlite3

# def inicializar_banco():
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#     cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS escolas (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT
#                         nome TEXT NOT NULL
#                         )
#                         ''')
#     conexao.commit()
#     # O banco não está salvando as alterações. Por que?
#     conexao.close()
#     # O banco não está salvando as alterações pois está faltando o conexao.commit()

    import sqlite3 

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL  
            )
        ''')

    conexao.commit() # o banco de dados nao foi criado
    conexao.close() 
