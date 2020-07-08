import pandas as pd
from pandas.errors import EmptyDataError
import os

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
    except FileNotFoundError:
        #Se o estoque.csv não existir, um novo arquivo será criado
        with open(os.path.join(os.getcwd(), "backend", "static", "pd", "estoque.csv"), "w"):
            #Além de um novo dataframe, o qual preencherá o estoque.csv
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