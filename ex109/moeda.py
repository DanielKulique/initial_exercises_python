#utilizando modularização e def de funções


def aumentar(valor = 0, porc = 0, form = False): #aumenta em tantos (%) o valor
    aum = valor + (valor * porc/100)
    if form:
        return moeda(aum)
    else:
        return aum


def diminuir(valor = 0, porc = 0, form = False): #reduz em tantos (%) o valor
    red = valor - (valor * porc/100)
    if form:
        return moeda(red)
    else:
        return red


def dobro(valor = 0, form = False): #dobra o valor
    dob = valor * 2
    if form:
        return moeda(dob)
    else:
        return dob


def metade(valor = 0, form = False): #divide o valor em 2
    meio = valor/2
    if form:
        return moeda(meio)
    else:
        return meio


def moeda(func):
    return f'R${func:.2f}'.replace('.', ',')