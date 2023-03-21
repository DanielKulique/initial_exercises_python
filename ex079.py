#listagem de número com escolha de parar ou continuar.


lnumber = []
while True:
    number = (int(input('Digite um valor: ')))
    if lnumber.count(number) == 0:
        lnumber.append(number)
    else:
        print('Número repetido. Não contabilizado!')
    while True:
        action = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        if action == 'S' or action == 'N':
            break
        else:
            print('Tente novamente. ', end='')
    if action == 'N':
        break
print(f'Você digitou os valores: {sorted(lnumber)}')
