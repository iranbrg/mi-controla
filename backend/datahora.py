import datetime

novo_produto_data_hora= {}

def hora(nome):
    data_hora = datetime.datetime.now()
    novo_produto_data_hora[nome]= data_hora.strftime("%d"+"/"+"%m"+"/"+"%Y"+" %X")
    return novo_produto_data_hora
    

