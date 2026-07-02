import sqlite3

def cadastrar_professor(nome,cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    # O sistema aceita cadastrar dois professores com o mesmo CPF.
    # Como restringir isso direto na estrutura da tabela abaixo?
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        cpf TEXT
                        )
                        ''')
    

import _sqlite3 

def cadastrar_professor (nome, cpf):
    conexao = _sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS professores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   cpf UNIQUE TEXT
                   )
                   ''')
    
# o erro era por que o cpf não estava unique e ele so pode ser unico 
# entao para não dar erro tem que colocar unique no cpf
