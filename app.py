from flask import Flask
from flask import render_template, url_for, request, redirect
# import connectDatabase

app = Flask(__name__)

##############################################################################
#                          CRUD SIMPLES >> CATEGORIAS                        #
##############################################################################
class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

cat1 = Categorias(123, 'Artes', 'randon text1')
cat2 = Categorias(213, 'Games', 'randon text2')
lista = [cat1,cat2]

# --------------------------------- EXIBIR --------------------------------- #
@app.route('/categoria')
def exibir():
    return render_template('homepage.html', titulo='Categorias', Categorias=lista)

# ------------------------------- ADICIONAR -------------------------------- #
@app.route('/categoria', methods=['POST',]) # ESTÁTICO !!!
def adicionar():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    cat3 = Categorias(id, nome,descricao)
    lista.append(cat3)
    return render_template('homepage.html', titulo='Categorias', Categorias=lista)

# --------------------------------- EDITAR --------------------------------- #
@app.route('/categoria')
def editar():
    pass

# --------------------------------- DELETAR -------------------------------- #
@app.route('/categoria')
def deletar():
    pass

app.run(debug=True)