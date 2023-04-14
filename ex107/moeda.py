#utilizando modularização e def de funções


def aumentar(valor, porc): #aumenta em tantos (%) o valor
    aum = valor + (valor * porc/100)
    return aum


def diminuir(valor, porc): #reduz em tantos (%) o valor
    red = valor - (valor * porc/100)
    return red


def dobro(valor): #dobra o valor
    dob = valor * 2
    return dob


def metade(valor): #divide o valor em 2
    meio = valor/2
    return meio
