from flask import Flask
from flask import render_template, url_for, request, redirect
# import connectDatabase

app = Flask(__name__)

class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

##############################################################################
#                             ROTAS PARA CATEGORIA                           #
##############################################################################
@app.route('/categoria')
def categoria():
    cat1 = Categorias(123, 'Artes', 'randon text1')
    cat2 = Categorias(213, 'Games', 'randon text2')
    cat3 = Categorias(321, 'Filmes', 'randon text3')
    lista = [cat1,cat2,cat3]
    return render_template('homepage.html', titulo='Categorias', Categorias=lista)


app.run(debug=True)
