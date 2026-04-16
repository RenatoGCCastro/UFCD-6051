# cilco principal

while True:
    #dados de entrada
    sensor_de_pressao = 35

    # prossesamento
    if sensor_de_pressao <= 40:
        activa_eletrovalvula = True
    else:
        activa_eletrovalvula = False
