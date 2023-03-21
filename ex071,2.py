#O produto mais barato e o mais caro.


print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar?'))
total = valor
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f' Total de {contced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
