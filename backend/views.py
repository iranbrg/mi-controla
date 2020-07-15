from flask import render_template, redirect, url_for, request   
from backend import app
from backend.forms import NovoProduto
from backend.pd import novo_produto, leitura_estoque


@app.route('/estoque')
def estoque():
    return render_template('estoque.html', title='Estoque', estoque=leitura_estoque())

@app.route('/adicionar', methods=['POST','GET'])
def adicionar():
    form = NovoProduto()
    if form.validate_on_submit():
        novo_produto(form)
        return redirect(url_for('estoque'))
    return render_template('adicionar.html', form=form)

@app.route('/historico')
def historico():
    return render_template('historico.html', estoque=leitura_estoque()) 

@app.route('/')
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] !='admin' or request.form['password'] != 'admin':
            error = ' Credenciais incorretas. Por favor, tente novamente.'
        else:
            return redirect(url_for('estoque'))
    return render_template('login.html', error=error) 

@app.route('/registro')
def registro():
    return render_template('registro.html')