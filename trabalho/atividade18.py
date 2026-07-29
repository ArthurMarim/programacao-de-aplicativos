# import sqlite3

# def cadastrar_lista_alunos():
#     lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 

# conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

#  #O comando executymany quebra com a mensagem: "Function takes exactly 2 arguments".
#  #Como passar a lista de dados da forma correta dentro dele? 
# cursor.execute("INSER INTO alunos (nome, id_turma) VALUES (?,?)", lista)

# conexao.commit()
# conexao.close()

import sqlite3

lista = [
    ("Ana", 1),
    ("Carlos", 1),
    ("Beatriz", 2)
]

conexao = sqlite3.connect("siste_escola.db")
cursor = conexao.cursor()

cursor.executemany(
    "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
    lista
)

conexao.commit()
conexao.close()

# O erro foi que usou o comando execute() ao invés de executemany().
