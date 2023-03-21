#posicionando valores em uma lista


lista = []
for r in range(0, 5):
    n = int(input('Digite o valor: '))
    if r == 0 or n >= lista[-1]:
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos}')
                break
            pos += 1
print(lista, 'FIM')
