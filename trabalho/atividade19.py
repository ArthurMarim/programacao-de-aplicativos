# import sqlite3
# def buscar_dados_dinamicos(nome_tabela, id_registro):
#     conexao = sqlite3.connect('sistema_escola.db')
#     cursor = conexao.cursor()

# # O SQLITE joga um erro de sintaxe operacional indicando que não aceita o caractere '?'.
# # Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança?
#     cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro))

#     print (cursor.fetchone())
#     conexao.close()

import sqlite3

def buscar_dados(nome_tabela, id_registro):
    tabelas_permitidas = {"alunos", "professores", "turmas"}

    if nome_tabela not in tabelas_permitidas:
        print("Tabela inválida.")
        return

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    sql = f"SELECT * FROM {nome_tabela} WHERE id = ?"
    cursor.execute(sql, (id_registro,))

    print(cursor.fetchone())

    conexao.close()
# O erro estava em usar um ? após o FROM, pois o SQlite não consegue identificar a tabela neste caso.
