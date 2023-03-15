#preço de passagem por Km


km = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(km))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
