from flask import Flask
from flask import render_template, url_for, request, redirect
from connectDatabase import Categorias

app = Flask(__name__)
sql = Categorias(None, None)

##############################################################################
#                          CRUD SIMPLES >> CATEGORIAS                        #
##############################################################################

# --------------------------------- EXIBIR --------------------------------- #
@app.route('/categoria')
def exibir():
    results = sql.get_all_categoria()
    print(results)
    return render_template('homepage.html', titulo='Categorias', Categorias=results)

# ------------------------------- ADICIONAR -------------------------------- #
@app.route('/categoria', methods=['POST',])
def adicionar():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    nova_categoria = sql.nova_categoria(nome, descricao)
    results = sql.get_all_categoria()
    return render_template('homepage.html', titulo='Categorias', Categorias=results)

# --------------------------------- EDITAR --------------------------------- #
@app.route('/categoria')
def editar():
    pass

# --------------------------------- DELETAR -------------------------------- #
@app.route('/categoria')
def deletar():
    pass

app.run(debug=True)