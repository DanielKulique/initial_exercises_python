#progressão aritmética com estrutura de controle


pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
print(f'\033[4;33mA PA começando em {pt} com razão de {rz} corresponde a: ')
i = 0
while i < 10: #= (pt + 9 * rz):
    i += 1
    print(pt, end=' ')
    pt = pt + rz
print('\033[0;32mFIM!')
