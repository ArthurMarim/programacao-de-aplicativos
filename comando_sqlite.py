import sqlite3

conexao = sqlite3.connect('sistema_hospital.db')
cursor = conexao.cursor()

cursor.execute('''
     DROP TABLE hospital
''')

conexao.commit()
