# import sqlite3

# def buscar_professor(id_prof):
#     conexao = sqlite3.connect
#     cursor = conexao.cursor()

#     # O python reclama de "Incorrect number of bindings".
#     # Estamos passando a variável, por que ocorre o erro?
#     cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof))
#     resultado = cursor.fetchone()
#     print(resultado)
#     conexao.close()
    

import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close
# É obrigatorio colocar a virgula dps do elemento 