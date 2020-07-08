from backend import app
from flask import render_template, redirect, url_for, flash
from backend.forms import NovoProduto

@app.route('/')
@app.route('/estoque')
def estoque():
    return render_template('estoque.html') 

@app.route('/adicionar', methods=['POST','GET'])
def adicionar():
    form = NovoProduto()
    if form.validate_on_submit():
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