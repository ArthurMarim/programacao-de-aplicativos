# import sqlite3

# def atualizar_nome_Aluno(id_aluno, novo_nome):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

# # O professor pediu para mudar o nome do aluno de ID 3,
# # Mas o sistema alterou o nome de TODOS os alunos do banco de dados! Correção urgente:
# cursor.execute("UPDATE alunos SET nome = ?", (novo_nome))

# conexao.commit()
# conexao.close()

import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE alunos SET nome = ? WHERE id = ?", (novo_nome, id_aluno))

    conexao.commit()
    conexao.close()

# Faltou usar o WHERE no UPDATE, então o sistema mudou o nome de todos os alunos e não só do aluno com o ID informado.