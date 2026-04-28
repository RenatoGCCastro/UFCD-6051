#### - Criar uma estrutura de dados com os componentes
# de um quadro eletrico á vossa escolha.
# menciona as especificações dos componentes

quadro_eletrico ={
    "corte_geral": {
        "in" : 32,
    },
    "diferencial": {
     "deltaI": 0.03,
     "in": 32,
    },
    "disjuntor1":
      {
        "in": 10
    },
    "disjuntor2":
    {
        "in": 16
    }
}

lampadas = {
    "potencia": 40,
    "tensao" : 230,
    "quantidade" : 3
}

import minhas_funcoes

corrente_de_cada_lampada = lampadas["potencia"] / lampadas["tensao"]
print(corrente_de_cada_lampada)
corrente_de_todas_as_lampadas = minhas_funcoes.calcular_corrente(lampadas["potencia"], lampadas["tensao"])
print(corrente_de_cada_lampada)

corrente_de_todas_as_lampadas = corrente_de_cada_lampada * lampadas["quantidade"]
corrente_de_todas_as_lampadas

minhas_funcoes.selecionar_disjuntor(corrente_de_todas_as_lampadas)
