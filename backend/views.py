import os
from flask import render_template, redirect, url_for, request
from backend import app
from backend.forms import NovoProduto, RetirarProduto, RemoverProduto
from backend.pd import novo_produto, leitura_estoque, retirar_produto, leitura_historico, remover
from backend.images import nova_imagem

# TODO: error pages

@app.route('/estoque/', methods=['POST','GET'])
def estoque():
    form = RetirarProduto()
    form_remover = RemoverProduto()

    if form.validate_on_submit():
        retirar_produto(form)
        return redirect(request.url)
    elif form_remover.validate_on_submit():
        remover(form_remover)
        return redirect(request.url)
        
    return render_template('estoque.html', estoque=leitura_estoque(), form=form, form_remover=form_remover)

@app.route('/adicionar/', methods=['POST','GET'])
def adicionar():
    form = NovoProduto()
    
    if form.validate_on_submit():
        foto_produto_nome = nova_imagem(form)
        novo_produto(form, foto_produto_nome)
            
        return redirect(url_for('estoque'))

    return render_template('adicionar.html', form=form)

@app.route('/historico/')
def historico():
    return render_template('historico.html', hist=leitura_historico())

@app.route('/', methods=['POST','GET'])
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] != 'admin':
            error = 'Credenciais incorretas. Por favor, tente novamente.'
        else:
            return redirect(url_for('estoque'))
    return render_template('login.html', error=error) 

@app.route('/registro/')
def registro():
    return render_template('registro.html')
