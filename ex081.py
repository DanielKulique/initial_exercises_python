#listagem de número em ordem descrescente


lista = []
print('-'*30)
cont = 0
while True:
    num = int(input('Digite o valor: ')) # entrada de valor
    if lista.count(num) == 0:
        lista.append(num)
        cont += 1
    else:
        print('Número repetido não contabilizado!')
    while True: #continuar ou não
        acao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if acao in 'SsNn':
            break
        else:
            print('Opção não identificada... ', end='')
    if acao in 'Nn': #para ou continuar a digitação
        break
clista = lista[:]
print('-'*30)
print(f'A lista {lista}')
print(f'>Possue [{cont}] números!')
clista.sort(reverse=True)
print(f'>Sua ordem decrescente é {clista}')
if lista.count(5) > 0:
    print(f'O valor 5 está na lista. Posição {lista.index(5)} da lista original!')
else:
    print(f'O valor 5 não está na lista!')
