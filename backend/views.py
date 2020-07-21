import os
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from backend import app
from backend.forms import NovoProduto, RetirarProduto, RemoverProduto
from backend.pd import novo_produto, leitura_estoque, retirar_produto, leitura_historico, remover

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
    
    path_to_foto_produto = os.path.join(os.path.dirname(app.instance_path), "backend", "static", "images", "produtos")

    if form.validate_on_submit():
        #TODO: Evitar o submit com a verificação do upload de 2 imagens com  mesmo nome
        #TODO: Produto sem foto

        foto_produto = form.imagem_produto.data
        foto_produto_nome = secure_filename(foto_produto.filename)
        # foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))
        foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))
        
        novo_produto(form, foto_produto_nome)
        
        # if foto_produto_nome in os.listdir(path_to_foto_produto):
        #     flash("Já há uma foto com esse nosse associada a um produto, renomei-a e repita o upload", "error")
        # else:
        #     foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))
            
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
