#aprimorando o sistema de cálculo PA


from time import sleep
pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
trm = int(input('Digite quando termos deseja verificar:'))
print(f'\033[33mA PA começando em {pt} com razão de {rz} corresponde a: \033[32m')
i = 0
cont = 0
while i < trm:
    i += 1
    print(pt, end=' ')
    pt = pt + rz
    cont += 1
    if trm == i:
        print('pausa')
        print(f'\033[32mForam verificados ao total {cont} termo!')
        acao = int(input('\033[33mverificar mais algum termo?: \033[32m'))
        if acao > 0:
            trm = trm + acao
        else:
            print('\033[31mFinalizando...')
            sleep(1)
            break
