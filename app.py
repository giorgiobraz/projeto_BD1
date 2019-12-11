from flask import Flask
from flask import render_template, url_for, request, redirect
from connectDatabase import Categorias, Produtos

app = Flask(__name__)
sql = Categorias(None, None)
sql2 = Produtos(None, None, None, None, None)

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
    return render_template('homepage.html', titulo='Categorias', Categorias=results)


# Deletar categoria
@app.route('/categoriadelete', methods=['POST',])
def deletar():
    id = request.form['id']
    rm = sql.rm_categoria(id=id)
    results = sql.get_all_categoria()
    return render_template('homepage.html', titulo='Categorias', Categorias=results)




###################################################################################
# 								    CRUD PRODUTOS                                 #
###################################################################################

# Exibir produtos
@app.route('/produto')
def exibir_produtos():
    results = sql2.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)

# Adicionar produtos
@app.route('/produto', methods=['POST',])
def adicionar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    qtde = request.form['qtde']
    secao = request.form['secao']
    categoria  = request.form['categoria']
    add = sql2.novo_produto(nome, descricao, qtde, secao, categoria)
    results = sql2.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)

# Editar produtos
@app.route('/atualizarproduto', methods=['POST',])
def editar_produto():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    qtde = request.form['qtde']
    secao = request.form['secao']
    categoria  = request.form['categoria']
    update = sql2.edit_nome_produto(id, nome, descricao, qtde, secao, categoria)
    results = sql2.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)


# Deletar produtos
@app.route('/produtodelete', methods=['POST',])
def deletar_produto():
    id = request.form['id']
    rm = sql2.rm_produto(id=id)
    results = sql2.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)

app.run(debug=True)