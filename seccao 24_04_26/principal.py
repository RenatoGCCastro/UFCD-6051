# lista material sala

mesa1 ={
    "tamanho" : {
        "comprimento" : 1000,
        "altura" : 900,
        "largura" : 800,
    },
    "material": [
        "ferro", 
        "madeira", 
    ],   
}
mesa2 ={
    "tamanho" : {
        "comprimento" : 500,
        "altura" : 900,
        "largura": 800,
    },
    "material" :[
        "ferro",
        "madeira"
    ],
}
cadeira ={
    "tamanho" :{
        "comprimento" : 450,
        "altura" : 900,
        "largura" : 450,
    },
    "material": {
        "ferro",
        "plastico",
    },
}

computadores ={
    "modelo": "hp",
    "impressora" : "hp",
    "teclado" : "hp"
}

quadro_branco ={
    "tamanho" : {
        "comprimento" : 1200,
        "largura" : 1750,
    }
}

quadro_interativo ={
    "tamanho" : {
        "comprimento"  : 900,
        "largura" : 1200,
    },
}

lista_de_objectos = [
    quadro_branco,
    quadro_interativo,
    cadeira * 25,
    mesa1 * 20,
    mesa2 * 5,
    computadores * 20,
]

