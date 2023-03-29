#número pares e impares em listas diferentes


lista = []
listapar = []
listaimpar = []
print('-'*30)
while True:
    num = int(input('Digite o valor: '))
    if lista.count(num) == 0:
        lista.append(num)
        if (num % 2) == 0:
            listapar.append(num)
        else:
            listaimpar.append(num)
    else:
        print('Número já foi digitado. Não contabilizado! ', end='')
    while True:
        acao = str(input('Deseja continuar?: [S/N]: ')).strip()[0]
        if acao in 'SsNn':
            break
        else:
            print('Opção não identificada... ', end='')
    if acao in 'Nn': #Loop parar ou continuar digitação
        break
print('-'*30)
print(f'A lista inteira é {lista}!')
print(f'A lista dos números pares é {listapar}!')
print(f'A lista dos números ímpares é {listaimpar}!')
