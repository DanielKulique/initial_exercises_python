#listagem de preço em tabela (com estrutura de repetição)


listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:                                #mostra apenas os itens pares da tupla (nomes dos itens)
        print(f'{listagem[pos]:.<40}R$', end='')    #pos = 2, 4, 6, 8, 10, 12, 14....
    else:                                           # se não! mostrar os itens ímpares (preços)
        print(f'{listagem[pos]:>8.2f}')             #pos = 1, 3, 5, 7, 9, 11.....
print('-'*50)