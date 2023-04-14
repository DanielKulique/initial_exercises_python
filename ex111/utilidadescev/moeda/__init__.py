def aumentar(valor = 0, porc = 0, form = False): #aumenta em tantos (%) o valor
    """
    -> Calcula o aumento de um determinado preço
    retornando o resultado com ou sem formatação
    :param valor: o preço que será analisado
    :param porc: porcentagem do aumento
    :param form: opção de formatação
    :return:
    """
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


def titulo(msg):
    tam = len(msg) + 12
    print('-' * tam)
    print(f'{msg:^{tam}} ')
    print('-' * tam)


def resumo(valor = 0, aum = 0, red = 0):
    titulo('RESUMO DO VALOR')
    print(f'Preço Analisado:    {moeda(valor)}.')
    print(f'Dobro do preço:     {moeda(dobro(valor))}.')
    print(f'Metade do preço:    {moeda(metade(valor))}.')
    print(f'{aum}% de aumento:     {moeda(aumentar(valor, aum))}.')
    print(f'{red}% de redução:     {moeda(diminuir(valor, red))}.')
    print('---------------------------')

