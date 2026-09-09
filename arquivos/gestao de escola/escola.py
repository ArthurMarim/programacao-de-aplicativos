def cadastrar_escolas():
    try:
        nome_escola = input("Qual escola deseja cadastrar:  ")
        cidade_escola = input("Digite a cidade da sua escola:  ")

        comando_inserir = '''INSERT INTO escolas (nome_escola , cidade_escola)
                                        VALUES (?,?)'''
                                    
        cursor.execute (comando_inserir, (nome_escola , cidade_escola))
        id_escola = cursor.lastrowid
        conexao.commit()
        assert id_escola is not None , "O ID da escola não foi gerado!"
        assert id_escola > 0 , "O ID da escola deve ser maior que 0"

        print ("Escola cadastrada com sucesso!")
        print (f"ID da escola {id_escola}")

    except sqlite3.IntegrityError:
        print("ERRO: Essa escola já está cadastrada!")
    finally:
        conexao.close()

def listar_escolas():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.execute('''
                            SELECT * FROM escolas
                            '''
                            )       
    todas_escolas = cursor.fetchall()
    if not todas_escolas:
        print("Nennhuma escola encontrada")
    else:
        for escola in todas_escolas:
            assert escola[0] is not None, "A escola não possui ID!"
            assert escola[1] != "", "O nome da escola está vazio!"
            assert escola[2] != "", "A cidade da escola está vazia!"
            print(f"ID: {escola[0]}, Escola: {escola[1]}, Cidade: {escola[2]} ") 
    conexao.close()

def atualizar_escolas():
    