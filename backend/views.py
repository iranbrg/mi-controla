from flask import render_template, redirect, url_for, request   
from backend import app
from backend.forms import NovoProduto
from backend.pd import novo_produto, leitura_estoque
from backend.datahora import hora
from werkzeug.utils import secure_filename
import os

@app.route('/estoque')
def estoque():
    return render_template('estoque.html', estoque=leitura_estoque())

@app.route('/adicionar', methods=['POST', 'GET'])
def adicionar():
    form = NovoProduto()
    if form.validate_on_submit():
        global hora_mod
        hora_mod = hora()
        novo_produto(form)
        f = form.foto.data
        filename = secure_filename(f.filename)
        if filename.endswith('.png'):
            f.save(os.path.join(os.getcwd(), "backend", "static", "images", "produtospng", filename))
            os.rename(os.path.join(os.getcwd(), "backend", "static", "images", "produtospng", filename), os.path.join(os.getcwd(), "backend", "static", "images", "produtospng", "{}.png".format(form.nome_produto.data)))
        else:
            f.save(os.path.join(os.getcwd(), "backend", "static", "images", "produtosjpg", filename))
            os.rename(os.path.join(os.getcwd(), "backend", "static", "images", "produtosjpg", filename), os.path.join(os.getcwd(), "backend", "static", "images", "produtosjpg", "{}.jpg".format(form.nome_produto.data)))   
        print(form.errors)
        return redirect(url_for('estoque'))
    return render_template('adicionar.html', form=form)


@app.route('/historico')
def historico():
    global hora_mod
    return render_template('historico.html', estoque=leitura_estoque(), data_hora=hora_mod) 

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

@app.route('/registro')
def registro():
    return render_template('registro.html')

# @app.route('/macros')
# def macros():
#     return render_template('macros.html', data_hora=hora())
