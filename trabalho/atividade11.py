# import sqlite3

# def listar_alunos_e_turmas():
#     conexao = sqlite3.conect('sistema_escola.db')
#     cursor = conexao.cursor()

#     # O relatória roda, mas repete os dados erroneamente em formato de matriz cruzada
#     #  Porque falta definir a regra de colagem (vinculo). Conserte o comando SQL:
#     cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas")
#     for linha in cursor.fetchall():
#         print (f"Aluno: {linha[0]} | Turma: {linha[1]}")
#         conexao.close()
        

import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute('''
            SELECT alunos.nome, turmas.nome_turma
            FROM alunos
            INNER JOIN turmas
            ON alunos.id_turma = turmas.id
        ''')

        alunos = cursor.fetchall()

        if alunos:
            print("\n=== Lista de Alunos e Turmas ===")
            for aluno in alunos:
                print(f"Aluno: {aluno[0]} | Turma: {aluno[1]}")
        else:
            print("Nenhum aluno encontrado.")

    except sqlite3.Error:
        print("Erro ao listar alunos e turmas.")

    finally:
        conexao.close()

listar_alunos_e_turmas()

import sqlite3

def criar_tabela_escolas():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_escola(nome):
    with sqlite3.connect("sistema_escola.db") as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome) VALUES (?)",
            (nome,)
        )

        conexao.commit()

        print("Escola cadastrada com sucesso!")

criar_tabela_escolas()

nome = input("Digite o nome da escola: ")

inserir_escola(nome)


# Faltava a condição ON para ligar alunos e turmas de forma correta. 
