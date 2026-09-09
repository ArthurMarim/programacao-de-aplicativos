def turmas_escola():
    try:
        nome_turma = input("Digite o nome da sua turma: ")
        id_escolas = int(input("Digite o id da escola: "))

        assert nome_turma.strip() != "", "O nome da turma não pode estar vazio!"
        assert id_escolas > 0, "O ID da escola deve ser maior que zero!"

        comando_inserir = '''
            INSERT INTO turmas (nome_turma, id_escolas)
            VALUES (?, ?)
        '''

        cursor.execute(comando_inserir, (nome_turma, id_escolas))
        conexao.commit()

        id_turma = cursor.lastrowid
        assert id_turma is not None, "A turma não foi cadastrada!"

        print("Turma cadastrada com sucesso!")
        print(f"ID da turma: {id_turma}")

    except sqlite3.IntegrityError:
        print("ERRO: A escola informada não existe!")

    except AssertionError as erro:
        print(f"ERRO DE VALIDAÇÃO: {erro}")

    finally:
        conexao.close()

def listar_turmas():
    conexao = sqlite3.connect('gestao_escolar.db')

    cursor = conexao.execute('''
        SELECT * FROM turmas
    ''')

    todas_turmas = cursor.fetchall()

    if not todas_turmas:
        print("Nenhuma turma encontrada")
    else:
        for turma in todas_turmas:

            assert turma[0] is not None, "A turma não possui ID!"
            assert turma[1] != "", "O nome da turma está vazio!"
            assert turma[2] is not None, "A turma não possui ID da escola!"

            print(f"ID: {turma[0]}, Turma: {turma[1]}, ID Escola: {turma[2]}")

    conexao.close()
