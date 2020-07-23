import os, re
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from backend import app

path_to_foto_produto = os.path.join(os.path.dirname(app.instance_path), "backend", "static", "images", "produtos")
produto_sem_imagem = "produto-sem-imagem.png"

def nova_imagem(form):
    foto_produto = form.imagem_produto.data

    # Verifica se o novo produto possui imagem
    if foto_produto == None:
        # Caso não tenha, lhe será atribuída a imagem "produto sem imagem" representada pela variável global "produto_sem_imagem"
        return produto_sem_imagem
    else:
        foto_produto_nome = secure_filename(foto_produto.filename)

        # Caso tenha, é verificado se já existe outra imagem salva com o mesmo nome
        if foto_produto_nome in os.listdir(path_to_foto_produto):
            # Antes de tudo, é mudado o nome da foto já existente na pasta
            # Com ReGex, é extraído o nome da imagem sem a sua extensão (e.g. .png, .jpg, etc...)
            match = re.search(r".+(?=\.\w+)", foto_produto_nome)
            foto_produto_nome_sem_ext = match.group(0)

            # A variável "i", após a execução do laço for, conterá o valor do total de repetições da nova imagem adicionada na pasta (se existirem outras)
            i = 0
            for foto in os.listdir(path_to_foto_produto):
                if re.search(foto_produto_nome_sem_ext + r"(\(\d+\))?", foto) != None:
                    i += 1

            # O novo nome da imagem existente na pasta será igual ao antigo acrescido de um número inteiro (e.g. nome_imagem(4).jpg)
            novo_foto_produto_nome = foto_produto_nome.replace(foto_produto_nome_sem_ext, f"{foto_produto_nome_sem_ext}({i})")

            os.rename(os.path.join(path_to_foto_produto, foto_produto_nome), os.path.join(path_to_foto_produto, novo_foto_produto_nome))

            foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))
        else:
            foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))

        return foto_produto_nome

    # if foto_produto_nome in os.listdir(path_to_foto_produto):
    #     flash("Já há uma foto com esse nosse associada a um produto, renomei-a e repita o upload", "error")
    # else:
    #     foto_produto.save(os.path.join(path_to_foto_produto, foto_produto_nome))

def remover_imagem(nome_imagem):
    from backend.pd import leitura_estoque, leitura_historico
    
    imagens_estoque = leitura_estoque()
    imagens_historico = leitura_historico()

    if imagens_estoque["imagem"].count(nome_imagem) == 1 and nome_imagem != produto_sem_imagem and nome_imagem not in imagens_historico["imagem"]:
        os.remove(os.path.join(path_to_foto_produto, nome_imagem))