#calculo porcentagem


print('Salário com 15% de aumento')
s = float(input('Digite o valor de seu salário em R$:'))
aum = s + (s * (15/100))
print('Sem novo salário com 15% de aumento é R${:.2f}'.format(aum))
