# ciclo principal
while True:
    # dados de entrada
    Sensor_da_porta = False
    Sinal_do_comando = False

    # processamento
    if not ((not sensor_da_porta and Sinal_do_comando) or (Sensor_da_porta and not Sinal_do_comando)):
        validar = True
    else:
        validar = False

        if not (Sensor_da_porta ^ Sinal_do_comando):
            ligar_luz : True
        else:
            ligar_luz : False
            
