#porcentagem


sal = float(input('Digíte o valor do seu salário em reais: ')) #sal = salário
if sal <= 1250:
    print(f'O valor de seu salário com aumento de 15% ficará em R${(sal*0.15)+sal}')
else:
    print(f'O seu salário com 10% de aumento ficará em R${(sal*0.10)+sal}')
