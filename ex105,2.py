#utilizando dicionário e definição de funções


def notas(*nota, sit=False):
    ficha = dict()
    ficha['TOTAL'] = len(nota)
    ficha['MAIOR'] = max(nota)
    ficha['MENOR'] = min(nota)
    ficha['MÉDIA'] = sum(nota)/len(nota)
    if sit:
        if ficha['MÉDIA'] >= 7:
                ficha['SITUAÇÃO'] = 'BOA'
        elif ficha['MÉDIA'] >= 5:
                ficha['SITUAÇÃO'] = 'RAZOÁVEL'
        else:
            ficha['SITUAÇÃO'] = 'RUIM'
    return ficha


# Programa Principal
resp = notas(6, 7, 3, 7)
print(resp)
