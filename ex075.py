#tratando dados na tupla.


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
listpar = []
tuplaN = (n1, n2, n3, n4)
print('Na tupla constituída por: ', end='')
for t in tuplaN:
    print(f'{t}', end=' ')
    if (t % 2) == 0:
        listpar.append(t)
print('\n',tuplaN.count(9), 'vezes apareceram o nº9')
if tuplaN.count(3) > 0:
    print(f' Na posição {tuplaN.index(3)+1} apareceu pela primeira vez o nº3')
else:
    print(' Não foi encontrado nenhum valor equivalente a 3 na tupla verificada!')
print(f' Os nº pares digitados são: {listpar}')
