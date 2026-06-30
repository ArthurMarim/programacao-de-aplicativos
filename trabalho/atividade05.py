import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    # Se o usuário digitar "Turma B" em vez de um numero de ID, o sistema quebra.
    # O try/except abaixo falhou em capturar esse erro. Qual o problema?
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.commit()
        except sqlite3.Error:
            print ("ERRO no banco de dados!")
        finally:
            conexao.close()
            