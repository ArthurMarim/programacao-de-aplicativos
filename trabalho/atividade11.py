import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.conect('sistema_escola.db')
    cursor = conexao.cursor()

    # O relatória roda, mas repete os dados erroneamente em formato de matriz cruzada
    #  Porque falta definir a regra de colagem (vinculo). Conserte o comando SQL:
    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas")
    for linha in cursor.fetchall():
        print (f"Aluno: {linha[0]} | Turma: {linha[1]}")
        conexao.close()
        

import sqlite3

def listar_alunos_e_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT alunos.nome, turmas.nome_turma
        FROM alunos 
        INNER JOIN turmas
        ON alunos.id_turma = turmas.id
    ''')

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
        conexao.close()

# Faltava a condição ON para ligar alunos e turmas de forma correta. 
