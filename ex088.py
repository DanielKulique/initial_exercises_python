#sorteio de 6 números sequencias


print('-'*31)
print(f'\033[33m{"JOGAR NA MEGA SENA":^30}\033[0m')
print('-'*31)
listcomb = list() #lista das 6 combinações
listseq = list() #lista das sequências
from random import randint
quant = int(input('\033[33mQuantos jogos você quer que eu sorteie?: '))
for r in range(0, quant):
    prmt = 1
    while prmt <= 6:
        comb = randint(0, 60)
        if listcomb.count(comb) == 0: #se não for encontrado a mesma combinação na lista
            listcomb.append(comb) #se adiciona a combinação gerada
            prmt += 1 # de modo a contabilizar a combinação
    listseq.append(listcomb[:])
    listcomb.clear()
from time import sleep
print('\033[32m-=-=-= SORTEANDO 10 JOGOS -=-=-=')
for e, seq in enumerate(listseq): #mostrar cada sequência gerada na lista randomizada
    print(f'Jogo {e+1}: {seq}')
    sleep(0.5)
print('-=-=-=-=-= BOA SORTE! -=-=-=-=-=')
