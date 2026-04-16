# ciclo principal

while True:
    # dados de entrada
    sensor_de_luz_1 = 5
    sensor_de_luz_2 = 5
    sensor_de_luz_3 = 5
    sensor_de_luz_4 = 5

    # processamento
    if sensor_de_luz_1 >= 5 or sensor_de_luz_2 >= 5 or sensor_de_luz_3 >= 5 or sensor_de_luz_4 >= 5:
        ativa_lampada = True
    else:
        ativa_lampada = False
