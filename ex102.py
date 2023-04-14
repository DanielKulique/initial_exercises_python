#utilizando docstrings, definindo função de fatorial.


def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor Fatorial de um número n.
    """
    cont = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        cont *= c
    print(cont)

num = int(input('Digite o valor: '))
while True:
    acao = str(input('Mostrar conta? [S/N]:  ')).upper()[0]
    if acao in 'SsNn':
        break
if acao in 'Ss':
    acao = True
else:
    acao = False
fatorial(num, acao)
help(fatorial)
