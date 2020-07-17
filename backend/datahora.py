import datetime

def hora():
    data_hora = datetime.datetime.now()
    return data_hora.strftime("%d"+"/"+"%m"+"/"+"%Y"+" %X")
    
