import os, datetime
import pandas as pd
from pandas.errors import EmptyDataError
from backend import app

path_to_estoque = os.path.join(os.path.dirname(app.instance_path), "backend", "static", "pd", "estoque.csv")

path_to_historico = os.path.join(os.path.dirname(app.instance_path), "backend", "static", "pd", "historico.csv")

def remover(form_remover):
    estoque_df = pd.read_csv(path_to_estoque)
    estoque_df.set_index("nome_produto", inplace=True)

    #Gravação da remoção do produto no histórico
    dados_produto_removido = {"nome_produto": form_remover.hidden_nome_produto.data, **estoque_df.loc[form_remover.hidden_nome_produto.data].to_dict()}
    historico(dados_produto_removido, status="removido")
    
    estoque_df.drop(index=form_remover.hidden_nome_produto.data, inplace=True)
    estoque_df.reset_index(inplace=True)
    estoque_df.to_csv(path_to_estoque, index_label=False, index=False)

def leitura_estoque():
    try:
        #Leitura do estoque.csv (criação do dataframe)
        estoque_df = pd.read_csv(path_to_estoque)
    except EmptyDataError:
        #Se o estoque.csv estiver vazio (sem produtos) a string é retornada
        return "estoque vazio"
    else:
        if not estoque_df.empty:
            return estoque_df.to_dict("list")
        else:
            return "estoque vazio"

def retirar_produto(form):
    estoque_df = pd.read_csv(path_to_estoque)
    estoque_df.set_index("nome_produto", inplace=True)
    
    #Verificação se a quantidade a ser retirada é menor ou igual à diponível no estoque
    if form.quantidadeR.data <= estoque_df.loc[form.hidden_nome_produto.data, "quantidade"]:
        #Gravação da retirada no histórico
        dados_produto_retirado = {"nome_produto": form.hidden_nome_produto.data, **estoque_df.loc[form.hidden_nome_produto.data].to_dict(), "quantidade": form.quantidadeR.data}
        historico(dados_produto_retirado, status="retirado")

        #Caso seja, ocorrerá o decremento da quantidade no estoque (estoque.csv) e uma mensagem de confimação será retornada
        estoque_df.loc[form.hidden_nome_produto.data, "quantidade"] -= form.quantidadeR.data
        estoque_df.reset_index(inplace=True)
        estoque_df.to_csv(path_to_estoque, index_label=False, index=False)
    
def novo_produto(form):
    dados_novo_produto = {"nome_produto": form.nome_produto.data.lower(),
                          "quantidade": form.quantidade.data,
                          "codigo_barras": form.codigo_barras.data,
                          "preco": form.preco.data,
                          "fornecedor": form.fornecedor.data,
                          "tempo_entrega": form.tempo_entrega.data,
                          "descricao": form.descricao.data.lower()}

    #Gravação do novo produto no histórico
    historico(dados_novo_produto, status="adicionado")

    try:
        #Leitura do estoque.csv (criação do dataframe)
        estoque_df = pd.read_csv(path_to_estoque)
    except EmptyDataError:
        #Se o estoque.csv existir, mas esteja vazio (sem produtos) um novo dataframe será criado
        estoque_df = pd.DataFrame([dados_novo_produto])
    else:
        estoque_df.set_index("nome_produto", inplace=True)

        #As condições verificam se existe um produto com os atributos iguais ao novo a ser adicionado. Caso exista, a quantidade do novo produto será somada à do produto já existente.
        if dados_novo_produto["nome_produto"] in estoque_df.index and dados_novo_produto["codigo_barras"] == estoque_df.loc[dados_novo_produto["nome_produto"], "codigo_barras"] and dados_novo_produto["preco"] == estoque_df.loc[dados_novo_produto["nome_produto"], "preco"] and dados_novo_produto["fornecedor"] == estoque_df.loc[dados_novo_produto["nome_produto"], "fornecedor"] and dados_novo_produto["tempo_entrega"] == estoque_df.loc[dados_novo_produto["nome_produto"], "tempo_entrega"]:
            estoque_df.loc[dados_novo_produto["nome_produto"], "quantidade"] += dados_novo_produto["quantidade"]
            
            estoque_df.reset_index(inplace=True)
        else:
            estoque_df.reset_index(inplace=True)
            #Do contrário, será adicionada uma nova linha ao dataframe (um novo produto)
            estoque_df = estoque_df.append(dados_novo_produto, ignore_index=True)
    finally:
        estoque_df.to_csv(path_to_estoque, index_label=False, index=False)

def historico(dados_produto, status=""):
    data_hora = datetime.datetime.now().strftime("%d"+"/"+"%m"+"/"+"%Y"+" %X")
    
    produto_his = {**dados_produto, "status": status, "data_hora": data_hora}

    try:
        #Leitura do historico.csv (criação do dataframe)
        historico_df = pd.read_csv(path_to_historico)
    except EmptyDataError:
        #Se o historico.csv existir, mas estiver vazio um novo dataframe será criado
        historico_df = pd.DataFrame([produto_his])
    else:
        #Do contrário, será adicionada uma nova linha ao dataframe (um novo registro no histórico)
        historico_df = historico_df.append(produto_his, ignore_index=True)
    finally:
        historico_df.to_csv(path_to_historico, index_label=False, index=False)

def leitura_historico():
    try:
        #Leitura do historico.csv (criação do dataframe)
        historico_df = pd.read_csv(path_to_historico)
    except EmptyDataError:
        #Se o estoque.csv estiver vazio (sem produtos) a string é retornada
        return "historico vazio"
    else:
        historico_df.sort_index(ascending=False, inplace=True)
        return historico_df.to_dict("list")