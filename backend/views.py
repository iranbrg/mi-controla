from flask import render_template, redirect, url_for, request
from backend import app
from backend.forms import NovoProduto, RetirarProduto
from backend.pd import novo_produto, leitura_estoque, retirar_produto

@app.route('/', methods=['POST','GET'])
@app.route('/estoque', methods=['POST','GET'])
def estoque():
    form = RetirarProduto()
    if form.validate_on_submit():
        retirar_produto(form)
        return redirect(request.url)
    return render_template('estoque.html', estoque=leitura_estoque(), form=form)

@app.route('/adicionar', methods=['POST','GET'])
def adicionar():
    form = NovoProduto()
    if form.validate_on_submit():
        novo_produto(form)
        return redirect(url_for('estoque'))
    return render_template('adicionar.html', form=form)

@app.route('/historico')
def historico():
    return render_template('historico.html') 


@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html') 

@app.route('/registro')
def registro():
    return render_template('registro.html')