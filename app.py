from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial para listar os produtos
@app.route('/')
def index():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

# Adicionar novo produto
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        imagem = request.form['imagem']

        conn = get_db_connection()
        conn.execute('INSERT INTO produtos (nome, preco, imagem) VALUES (?, ?, ?)', (nome, preco, imagem))
        conn.commit()
        conn.close()

        return redirect('/')
    
    return render_template('create.html')

# Rodar o servidor
if __name__ == '__main__':
    app.run(port=4000, debug=True)
