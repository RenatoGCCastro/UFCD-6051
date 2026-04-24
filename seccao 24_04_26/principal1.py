config = {
    "produtos" : {
        "café longo" : {
            "preço" : 0.5,
            "tem palheta" : True,
            "nivel acucar" : 2,
            "tem copo" : True,
            "botao_cafe_longo": "periferico_2",
        },
        "café longo" : {
            "preço" : 0.55,
        },
        "cappucino" : {
            "preço" : 0.8,
        },
        "chocolate" : {
            "preço" : 0.8,
        },
        "chá" : {
            "preço" : 0.4,
        },

    }
}
config["produtos"]
config["produtos"]["chá"]
preco_do_chocolate = config["produtos"]["chá"]["preço"]


conf_da_maquina = {
    "velocidade"
}


botao_cafe_longo = config["produto"]["cafe longo"]["botao_cafe_longo"]

# ciclo principal
while True:
    #ddos de entrada
    velocidade_da_maquina = config_da_maquina["velocidade"]

    # processamento
    if botao_cafe_longo and dinheiro_certo:
        if config["produto"]["cafe longo"]["tem_copo"]:
            colocar_copo()
        else:
            nao_colocar_copo()

        if botao_tirar_acucar :
            if config["produtos"]["cafe longo"]["nivel_de_acucar"] > 0:
                config["produtos"]["cafe longo"]["nivel_de_acucar"] -= 1
