import sqlite3
from banco import conectar


def cadastrar_escola():
    nome = input("Nome da escola: ")
    cidade = input("Cidade: ")

    assert nome != "", "O nome não pode ser vazio!"
    assert cidade != "", "A cidade não pode ser vazia!"

    try:
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )

        banco.commit()
        banco.close()

        print("Escola cadastrada com sucesso!")

    except sqlite3.Error:
        print("Erro ao cadastrar escola!")


def listar_escolas():
    try:
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM escolas")

        escolas = cursor.fetchall()

        print("\n--- ESCOLAS ---")

        if len(escolas) == 0:
            print("Nenhuma escola cadastrada.")

        for escola in escolas:
            print(
                "ID:", escola[0],
                "| Nome:", escola[1],
                "| Cidade:", escola[2]
            )

        banco.close()

    except sqlite3.Error:
        print("Erro ao listar escolas!")

