import pandas as pd
from pandas.errors import EmptyDataError
import os

def leitura_estoque():
    try:
        #Leitura do estoque.csv (criação do dataframe)
        estoque_df = pd.read_csv(os.path.join(os.getcwd(), "backend", "static", "pd", "estoque.csv"))
    except EmptyDataError:
        #Se o estoque.csv estiver vazio (sem produtos) a string é retornada
        return "estoque vazio"
    else:
        return estoque_df.to_dict("list")

def retirar_produto(form):
    estoque_df = pd.read_csv(os.path.join(os.getcwd(), "backend", "static", "pd", "estoque.csv"))
    estoque_df.set_index("nome_produto", inplace=True)
    
    
    #Verificação se a quantidade a ser retirada é menor ou igual à diponível no estoque
    if form.quantidadeR.data <= estoque_df.loc[form.hidden_nome_produto.data, "quantidade"]:
        #Caso seja, ocorrerá o decremento da quantidade no estoque (estoque.csv) e uma mensagem de confimação será retornada
        estoque_df.loc[form.hidden_nome_produto.data, "quantidade"] -= form.quantidadeR.data
        estoque_df.reset_index(inplace=True)
        estoque_df.to_csv(os.path.join(os.getcwd(), "backend", "static", "pd", "estoque.csv"), index_label=False, index=False)
        return True, "Produto retirado com sucesso"
    #Do contrário, não há decremento e uma mensagem de erro será retornada com o máximo de unidades que o usuário poderá retirar.
    elif form.quantidadeR.data > estoque_df.loc[form.hidden_nome_produto.data, "quantidade"]:
        return False, f"Pode-se retirar no máximo {estoque_df.loc[form.hidden_nome_produto.data, 'quantidade']} unidades"
    
def novo_produto(form):
    dados_novo_produto = {"nome_produto": form.nome_produto.data.lower(),
                          "quantidade": form.quantidade.data,
                          "codigo_barras": form.codigo_barras.data,
                          "preco": form.preco.data,
                          "fornecedor": form.fornecedor.data,
                          "tempo_entrega": form.tempo_entrega.data,
                          "descricao": form.descricao.data.lower()}

    try:
        #Leitura do estoque.csv (criação do dataframe)
        estoque_df = pd.read_csv(os.path.join(os.getcwd(), "backend", "static", "pd", "estoque.csv"))
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
        estoque_df.to_csv(os.path.join(os.getcwd(), "backend", "static", "pd", "estoque.csv"), index_label=False, index=False)