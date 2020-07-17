from flask import render_template, redirect, url_for, request, flash
from backend import app
from backend.forms import NovoProduto, RetirarProduto
from backend.pd import novo_produto, leitura_estoque, retirar_produto, leitura_historico
from backend.datahora import hora

@app.route('/', methods=['POST','GET'])
@app.route('/estoque/', methods=['POST','GET'])
def estoque():
    form = RetirarProduto()

    if form.validate_on_submit():
        is_maximo, msg_maximo = retirar_produto(form)
        if is_maximo:
            flash(msg_maximo, "success")
            return redirect(request.url)
        else:
            flash(msg_maximo, "error")

    return render_template('estoque.html', estoque=leitura_estoque(), form=form)

@app.route('/adicionar/', methods=['POST','GET'])
def adicionar():
    form = NovoProduto()
    if form.validate_on_submit():
        novo_produto(form)
        return redirect(url_for('estoque'))
    return render_template('adicionar.html', form=form)

@app.route('/historico/')
def historico():
    return render_template('historico.html', hist=leitura_historico())

@app.route('/login/', methods=['POST','GET'])
def login():
    return render_template('login.html') 

@app.route('/registro/')
def registro():
    return render_template('registro.html')