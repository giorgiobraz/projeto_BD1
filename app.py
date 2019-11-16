from flask import Flask
from flask import render_template, url_for, request, redirect

app = Flask(__name__)

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