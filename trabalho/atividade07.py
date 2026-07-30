# import sqlite3

# def cadastrar_turma(nome, id_serie, id_prof):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()
#     cursor.execute("PRAGMA foreign_keys = ON;")
#     # Se o id_prof não existir, ocorre um IntegrityError.
#     # Se o erro acontecer, o que ocorre com a linha conexao.close()?
#     cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?,?,?)", (nome, id_serie, id_prof))
#     conexao.commit()
#     conexao.close()
    

import sqlite3

def criar_tabelas_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            id_serie INTEGER,
            id_prof INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id),
            FOREIGN KEY (id_prof) REFERENCES professores(id)
        )
    ''')

    conexao.commit()
    conexao.close()
def cadastro_professor():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO professor (nome,id_serie) VALUES (?,?)", (nome,id_serie)
    )
    conexao.commit()
    print ("Professor cadastrado com sucesso!")

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute('''
            INSERT INTO turma (nome, id_serie, id_prof)
            VALUES (?, ?, ?)
        ''', (nome, id_serie, id_prof))

        conexao.commit()
        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: professor ou série não existe.")

    finally:
        conexao.close()

criar_tabelas_turma()

cadastrar_turma("Turma A", 1,1)
