#utilizando modularização e def de funções


def aumentar(valor = 0, porc = 0): #aumenta em tantos (%) o valor
    aum = valor + (valor * porc/100)
    return aum


def diminuir(valor = 0, porc = 0): #reduz em tantos (%) o valor
    red = valor - (valor * porc/100)
    return red


def dobro(valor = 0): #dobra o valor
    dob = valor * 2
    return dob


def metade(valor = 0): #divide o valor em 2
    meio = valor/2
    return meio


def moeda(func):
    return f'R${func:.2f}'.replace('.', ',')
