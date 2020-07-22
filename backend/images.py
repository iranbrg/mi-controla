import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from backend import app

path_to_foto_produto = os.path.join(os.path.dirname(app.instance_path), "backend", "static", "images", "produtos")
produto_sem_imagem = "produto-sem-imagem.png"

def nova_imagem(form):
    #TODO: Evitar o submit com a verificação do upload de 2 imagens com  mesmo nome
    #TODO: Produto sem foto

    foto_produto = form.imagem_produto.data

    if foto_produto == None:
        return produto_sem_imagem
    else:
        foto_produto_nome = secure_filename(foto_produto.filename)
        foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))
        
        return foto_produto_nome

    # if foto_produto_nome in os.listdir(path_to_foto_produto):
    #     flash("Já há uma foto com esse nosse associada a um produto, renomei-a e repita o upload", "error")
    # else:
    #     foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))

def remover_imagem(nome_imagem):
    # TODO: verificar se há produtos com imagens de mesmo nome antes de deletá-las
    os.remove(os.path.join(path_to_foto_produto, nome_imagem))