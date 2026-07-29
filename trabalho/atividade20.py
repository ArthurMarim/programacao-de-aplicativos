# import sqlite3 
 
# def cadastrar_escola_manual(): 
# 	# O aluno resolveu gerar o ID por conta própria 
#     id_escola = int(input("Digite o ID para a nova escola: ")) 
# 	nome = input("Nome da escola: ") 
     
#     conexao = sqlite3.connect('sistema_escola.db') 
# 	cursor = conexao.cursor() 
     
# 	# Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash). 
# 	# Aplique a blindagem protetora necessária: 
#     cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
     
#     conexao.commit() 
#     conexao.close() 

# O erro acontece pois o ID costuma ser uma PRIMARY KEY, e se o usuário informar um ID que já existe, ele da erro e o sistema é encerrado. 

import sqlite3

def cadastro_escola():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )
        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: já existe uma escola cadastrada com esse ID.")

    finally:
        conexao.close()

cadastro_escola()
