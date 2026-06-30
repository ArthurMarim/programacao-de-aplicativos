import sqlite3
def criar_tabelas():
    conexao = sqlite4.connect('sistema_escola.db')
    cursor = conexao.cursor()
    # Este bloco quebra ao rodar pela primeira vez em um banco limpo. Por que?
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS escolas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_serie TEXT,
                        id_escola INTEGER,
                        FOREIGN KEY (id_escola) REFERENCES escola(id)
                        )

                        ''')
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS escolas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT
                    )
                    ''')
    conexao.commit()
    conexao.close()
    