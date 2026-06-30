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
        