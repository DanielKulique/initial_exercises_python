#calculo porcentagem


print('Desconto de 5%')
p = float(input('Digíte o preço do produto em R$:'))
des = p - (p * (5/100))
print('O novo valor desse produto com 5% de desconto é R${:.2f}'.format(des))
