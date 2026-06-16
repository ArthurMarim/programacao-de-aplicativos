import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS professores(
               id_professores integer primary key autoincrement,
               nome_professores text not null,
               materia_professores text,
               idade_professores integer,
               cpf_professores text unique not null,
               salario_professores real not null,
               escola_professores text not null)''')

nome_completo = input("Digite seu nome completo: ")
materia = input("Digite a matéria que deseja: ")
idade = input("Digite a sua idade: ")
cpf = input("Digite seu CPF completo: ")
salario = input("Digite seu salário: ")
escola = input("Digite qual escola você da aula: ")

comando_inserir = f'''INSERT INTO professores (nome_professores, materia_professores, idade_professores, cpf_professores, salario_professores, escola_professores)
                      VALUES ('{nome_completo}','{materia}','{idade}','{cpf}','{salario}','{escola}')'''
cursor.execute (comando_inserir)
conexao.commit()
conexao.close()

def listar_professores():
    import sqlite3
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao_cursor()
    cursor.execute (''' SELECT * FROM professores''')
