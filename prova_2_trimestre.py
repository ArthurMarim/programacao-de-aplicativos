import sqlite3

def cadastrar_hospital():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS hospital (
                    id_hospital INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    nome_hospital TEXT NOT NULL,
                    cidade_hospital TEXT NOT NULL
                    )
                    '''
                    )
    nome_hospital = input("Digite qual o nome do hospital: ") 
    cidade_hospital = input("Digite a cidade que está localizado o hospital: ")

    comando_inserir = f'''INSERT INTO hospital (nome_hospital, cidade_hospital)
                        VALUES('{nome_hospital}','{cidade_hospital}')'''
    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

cadastrar_hospital()
print ("Seu Hospital foi cadastrado com sucesso!")

def cadastrar_medico():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    conexao.execute('''
                    CREATE TABLE IF NOT EXISTS medico (
                    id_medico INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    nome_medico TEXT NOT NULL,
                    crm_medico TEXT UNIQUE NOT NULL,
                    id_hospital INTEGER,
                    FOREIGN KEY (id_hospital) REFERENCES hospital(id_hospital)
                    )
                    '''                    
                    )
    nome_medico = input("Digite qual o seu nome: ")
    crm_medico = int(input("Digite qual o seu CRM: "))
    id_hospital = int(input("Qual o ID do seu hospital: "))

    comando_inserir = f'''INSERT INTO medico (nome_medico, crm_medico, id_hospital)
                          VALUES ('{nome_medico}','{crm_medico}','{id_hospital}')'''
    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

cadastrar_medico()
print ("Médico cadastrado com sucesso!")
