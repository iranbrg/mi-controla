from backend import app
from flask import render_template


@app.route('/')
@app.route('/estoque')
def estoque():
    return render_template('estoque.html', title='Estoque') 

@app.route('/adicionar', methods=['POST','GET'])
def adicionar():
    return render_template('adicionar.html', title='Adicionar ') 

@app.route('/historico')
def historico():
    return render_template('historico.html', title='Histórico') 

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html', title='Login') 

@app.route('/registro')
def registro():
    return render_template('registro.html', title='Registro') 


