def nome_alunos():
    try:
        nome_aluno = input("Digite seu nome: ")
        id_escola = int(input("Digite o id da escola: "))

        # Validações
        assert nome_aluno.strip() != "", "O nome do aluno não pode estar vazio!"
        assert id_escola > 0, "O ID da escola deve ser maior que zero!"

        comando_inserir = '''
            INSERT INTO alunos (nome_aluno, id_escola)
            VALUES (?, ?)
        '''

        cursor.execute(comando_inserir, (nome_aluno, id_escola))
        conexao.commit()

        id_aluno = cursor.lastrowid

        assert id_aluno is not None, "Aluno não foi cadastrado!"

        print("Aluno cadastrado com sucesso!")
        print(f"ID do aluno: {id_aluno}")

    except sqlite3.IntegrityError:
        print("ERRO: A escola informada não existe!")

    except AssertionError as erro:
        print(f"ERRO DE VALIDAÇÃO: {erro}")

    except ValueError:
        print("ERRO: Digite um número válido para o ID da escola!")

    finally:
        conexao.close()


def listar_alunos():
    conexao = sqlite3.connect('gestao_escolar.db')

    cursor = conexao.execute('''
        SELECT * FROM alunos
    ''')

    todos_alunos = cursor.fetchall()

    if not todos_alunos:
        print("Nenhum aluno encontrado!")
    else:
        for aluno in todos_alunos:

            assert aluno[0] is not None, "O aluno não possui ID!"
            assert aluno[1].strip() != "", "O nome do aluno está vazio!"
            assert aluno[2] is not None, "O aluno não possui ID da escola!"

            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, ID Escola: {aluno[2]}")

    conexao.close()
