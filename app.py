from flask import Flask
from flask import render_template, url_for, request, redirect
from connectDatabase import Categorias

app = Flask(__name__)
sql = Categorias(None, None)

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
@app.route('/categoria', methods=['POST',])
def editar():
    id = request.args.get('id')
    nome = request.form['nome']
    descricao = request.form['descricao']
    update = sql.edit_nome_categoria(id, nome, descricao)
    results = sql.get_all_categoria()
    return render_template('homepage.html', titulo='Categorias', Categorias=results)


# Deletar categoria
@app.route('/categoria')
def deletar():
    pass


###################################################################################
# 								    CRUD PRODUTOS
###################################################################################

# Exibir produtos
@app.route('/produto')
def exibir():
    results = sql.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)


# Adicionar produto
@app.route('/produto', methods=['POST',])
def adicionar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    qtde = request.form['qtde']
    secao = request.form['secao']
    id_categoria = request.form['id_categoria']
    add = sql.novo_produto(nome, descricao, qtde, secao, id_categoria)
    results = sql.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)


# Editar produto
@app.route('/produto', methods=['POST',])
def editar():
    id = request.args.get('id')
    nome = request.form['nome']
    descricao = request.form['descricao']
    qtde = request.form['qtde']
    secao = request.form['secao']
    id_categoria = request.form['id_categoria']
    update = sql.edit_nome_produto(id, nome, descricao)
    results = sql.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)


# Deletar produto
@app.route('/produto')
def deletar():
    pass

app.run(debug=True)