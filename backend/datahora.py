import datetime

def hora():
    data_hora = datetime.datetime.now()
    print (data_hora.strftime("%d"+"/"+"%m"+"/"+"%Y"+" %X"))
    
