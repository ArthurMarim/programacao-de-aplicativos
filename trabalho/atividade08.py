# import sqlite3

# def cadastrar_professor(nome,cpf):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()
#     # O sistema aceita cadastrar dois professores com o mesmo CPF.
#     # Como restringir isso direto na estrutura da tabela abaixo?
#     cursor.execute('''
#                     CREATE TABLE IF NOT EXISTS professores ( 
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         nome TEXT,
#                         cpf TEXT
#                         )
#                         ''')
    

import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS professores
    """)

    
    cursor.execute("""
    CREATE TABLE professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL
    )
    """)

    conexao.commit()

    cursor.execute("""
    INSERT INTO professores (nome, cpf)
    VALUES (?, ?)
    """, ("Gabriel Moya", "99999999999"))

    conexao.commit()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("Lista de Professores:")
    for professor in professores:
        print(professor)

    conexao.close()

cadastrar_professor("Gabriel Moya", "99999999999")  


# o erro era por que o cpf não estava unique e ele so pode ser unico 
# entao para não dar erro tem que colocar unique no cpf
