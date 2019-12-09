from flask import Flask
from flask import render_template, url_for, request, redirect
#from connectDatabase import Categorias
from connectDatabase import Produtos

app = Flask(__name__)
sql = Categorias(None, None)

app = Flask(__name__)
sql = Produtos(None, None, None, None, None)

###################################################################################
# 								    CRUD CATEGORIAS
###################################################################################

# Exibir categoria
@app.route('/categoria')
def exibir():
    results = sql.get_all_categoria()
    return render_template('homepage.html', titulo='Categorias', Categorias=results)

# Adicionar categoria
@app.route('/categoria', methods=['POST',])
def adicionar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    add = sql.nova_categoria(nome, descricao)
    results = sql.get_all_categoria()
    return render_template('homepage.html', titulo='Categorias', Categorias=results)

# Editar categoria
@app.route('/atualizarcategoria', methods=['POST',])
def editar():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    update = sql.edit_nome_categoria(id, nome, descricao)
    results = sql.get_all_categoria()
    print("MEU ID EDITAR: ")
    print(id)
    return render_template('homepage.html', titulo='Categorias', Categorias=results)


# Deletar categoria
@app.route('/categoriadelete', methods=['POST',])
def deletar():
    id = request.form['id']
    rm = sql.rm_categoria(id=id)
    results = sql.get_all_categoria()
    print("MEU ID: ")
    print(id)
    return render_template('homepage.html', titulo='Categorias', Categorias=results)


app.run(debug=True)

###################################################################################
# 								    CRUD PRODUTOS                                 #
###################################################################################

# # Exibir produtos
@app.route('/produto')
def exibir():
    results = sql.get_all_produto()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)

# # Adicionar produto
@app.route('/produto', methods=['POST',])
def adicionar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    secao = request.form['secao']
    idCategoria = request.form['idCategoria']
    add = sql.novo_produto(nome, descricao, quantidade, secao, id_categoria)
    results = sql.get_all_produto()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)

# # Editar produto
@app.route('/produto', methods=['POST',])
def editar():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    secao = request.form['secao']
    idCategoria = request.form['idCategoria']
    update = sql.edit_nome_produto(id, nome, descricao, quantidade, secao, id_categoria)
    results = sql.get_all_produto()
    print("MEU ID EDITAR: ")
    print(id)
    return render_template('produtos.html', titulo='Produtos', Produtos=results)

# # Deletar produto
@app.route('/produto')
def deletar():
    id = request.form['id']
    rm = sql.rm_produto(id=id)
    results = sql.get_all_produto()
    print("MEU ID: ")
    print(id)
    return render_template('produto.html', titulo='Produtos', Produtos=results)


app.run(debug=True)