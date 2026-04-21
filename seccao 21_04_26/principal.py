#### operações com numeros
# +
# -
# *
# /
# % -> resto
# **-> exponencial

# +
valor1 = 10
Valor2 = 15

soma = valor1 + Valor2
print(soma)

# -

valor1 = 50
valor2 = 25

resto = valor1 - valor2
print(resto)

# *

valor1 = 3
valor2 = 5

multiplica = valor1 * valor2
print(multiplica)

# /

valor1 = 50
valor2 = 25

divide = valor1 / valor2
print(divide)

# % 

valor1 = 250
valor2 = 15

restante = valor1 % valor2
print(restante)

 # **

valor1 = 3
valor2 = 5

elevado = valor1 ** valor2
print(elevado)


# *

iva = 1.23
preco_sem_iva = 100

preco_com_iva = preco_sem_iva * iva
print(preco_com_iva)

# media

segunda = 25
terça = 15
quarta = 20
quinta = 10
sexta =30

media = (segunda + terça + quarta + quinta +sexta) / 5
print(media)


testar_numero_de_vendas = segunda - media

if testar_numero_de_vendas > 0:
    print("dia bom")
else:
    print("dia mau")
