import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute (''' CREATE TABLE IF NOT EXISTS alunos (id_aluno integer primary key autoincrement,
                nome_aluno text NOT NULL,
                telefone_aluno TEXT,
                turma_aluno TEXT,
                idade_aluno INTEGER,
                cpf_aluno text UNIQUE NOT NULL)''')
nome_aluno = input("Digite o nome do aluno: ") 
telefone_aluno = input("Digite o telefone do aluno: ")
turma_aluno = input("Digite a turma do aluno: ")
idade_aluno = int(input("Digite a idade do aluno: "))
cpf_aluno = input("Digite o CPF do aluno: ")

comando_inserir = f'''INSERT INTO alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno)
                      VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{cpf_aluno}')'''

cursor.execute(comando_inserir)
conexao.commit()

print ("Seus dados foram atualizados")
cursor = conexao.cursor()
cursor.execute('''SELECT * FROM alunos''')
todos_alunos = cursor.fetchall()
if not todos_alunos:
    print("Nenhum aluno encontrado")
else:
    for aluno in todos_alunos:
        print(f"id: {aluno[0]}, nome: {aluno[1]}, telefone: {aluno[2]}, turma: {aluno[3]}, idade: {aluno[4]}, cpf: {aluno[5]}")
conexao.close()