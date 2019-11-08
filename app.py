from flask import Flask
from flask import render_template, url_for, request, redirect

app = Flask(__name__)

##############################################################################
class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

class Produtos:
    def __init__(self, codigo, nome, descricao, qtde, secao, id_categoria):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.qtde = qtde
        self.secao = secao
        self.id_categoria = id_categoria # FK

##############################################################################
@app.route('/produtos')
def produtos():
    return redirect(url_for('index'))

@app.route('/novo_produto')
def novo_produto():
    return redirect(url_for('index'))


@app.route('/categoria')
def categoria():
    return redirect(url_for('index'))

@app.route('/nova_categoria')
def nova_categoria():
    return redirect(url_for('index'))


app.run(debug=True)