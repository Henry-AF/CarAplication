import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Criar a tabela de produtos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        imagem TEXT
    )
''')

connection.commit()
connection.close()

print("Banco de dados criado com sucesso!")
