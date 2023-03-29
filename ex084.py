#maior e menor peso das pessoas informadas.


dados = list() #lista temporária
grupo = list()
cadastros = maipeso = menpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    grupo.append(dados[:]) #[:] fatiamento total
    dados.clear()
    cadastros += 1
    while True:
        acao = str(input('Deseja continuar? [S/N]: ')).strip()[0]
        if acao in 'SsNn':
            break
        else:
            print('Opção não identificada... ', end='')
    if acao in 'Nn':
        break
print(f'O total de pessoas registradas foram: {cadastros}')
pesadas = list()
leves = list()
for e, p in enumerate(grupo):
    if e == 0:
        maipeso = p[1]
        menpeso = p[1]
        pesadas.append(p[:])
        leves.append(p[:])
    else:
        if p[1] >= maipeso:
            maipeso = p[1]
        if p[1] <= menpeso:
            menpeso = p[1]
print(f'Maior peso: {maipeso}Kg, pessoas: ', end='')
for dados in grupo:
    if dados[1] == maipeso:
        print(f'[{dados[0]}]', end=' ')
print(f'\nMenor peso: {menpeso}Kg, pessoas: ', end='')
for dados in grupo:
    if dados[1] == menpeso:
        print(f'[{dados[0]}]', end=' ')
print(f'\nO total de cadastros foram: {len(grupo)}!')

