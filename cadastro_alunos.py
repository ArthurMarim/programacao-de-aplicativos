import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute (''' create table if not exists alunos(id_aluno integer primary key autoincrement,
                nome text not null,
                telefone text,
                turma text,
                idade integer,
                cpf text unique not null)''')
nome_aluno = input("Digite o nome do aluno: ") 
telefone_aluno = input("Digite o telefone do aluno: ")
turma_aluno = input("Digite a turma do aluno: ")
idade_aluno = int(input("Digite a idade do aluno: "))
cpf_aluno = input("Digite o CPF do aluno: ")

comando_inserir = f'''insert into alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno)
                    values('{nome_aluno}','{telefone_aluno}','{turma_aluno},'{idade_aluno}'.'{idade_aluno}','{cpf_aluno}')'''

cursor.execute(comando_inserir)
conexao.commit()
conexao.close()
