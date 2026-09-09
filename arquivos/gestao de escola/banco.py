import sqlite3

def escolas():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute (''' PRAGMA foreign_keys = ON; ''')
        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS escolas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_escola TEXT NOT NULL,
                            cidade_escola TEXT UNIQUE NOT NULL
                            )
                            '''
                        )
def turmas_escola():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute ('''PRAGMA foreign_keys = ON''')
        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS turmas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_turma TEXT NOT NULL,
                            id_escolas INTEGER NOT NULL,
                            FOREIGN KEY (id_escolas) REFERENCES escolas(id)
                            )
                            '''
                        )

def alunos_escola():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute ('''PRAGMA foreign_keys = ON''')
        cursor.execute ('''
                        CREATE TABLE IF NOT EXISTS alunos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_aluno TEXT NOT NULL,
                            id_escola INTEGER NOT NULL,
                            FOREIGN KEY (id_escola) REFERENCES escolas(id)
                            )
                            '''
                        )


