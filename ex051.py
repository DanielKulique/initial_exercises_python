#progressão aritmética


pt = int(input('\033[33mDigite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
print(f'\033[4;33mA PA começando em {pt} e com razão de {rz} compreende-se em:\033[0;32m')
decimo = pt + (10 - 1) * rz
for c in range(pt, decimo + rz, rz):
    print(c, end=' ')
print('acabou')
