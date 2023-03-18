#O produto mais barato e o mais caro.


total = menor = cont1000 = cont = 0
barato = ''
listpreco = []
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    cont += 1
    listpreco.append(preco)
    total += preco
    if preco > 1000:
        cont1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    while True:
        acao = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if acao == 'S' or acao == 'N':
            break
    if acao == 'N':
        break
print(f'\033[33mO total da compra foi R${total}\nTemos {cont1000} produtos custando mais que R$1000.00\n'
      f'O produto mais barato foi {barato} e custa R${min(listpreco)}')
