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




###################################################################################
# 								    CRUD PRODUTOS
###################################################################################

# Exibir produtos
@app.route('/produto')
def exibir_produtos():
    results = sql2.get_all_produtos()
    return render_template('produtos.html', titulo='Produtos', Produtos=results)





app.run(debug=True)