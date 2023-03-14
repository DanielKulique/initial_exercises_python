#randomização de números


from random import randint
from time import sleep
sort = randint(0, 5)
print('\033[34m-=-\033[m'*18)
print('\033[33m  Vou pensar em um número de 0 a 5. Tente acertar...\033[m')
print('\033[34m-=-\033[m'*18)
esc = int(input('\033[33mDigíte um número de sua escolha: \033[m'))
print('\033[4;33mPROCESSANDO...\033[m')
sleep(2)
if esc == sort:
    print('\033[32mParabéns você ganhou!\033[m')
else:
    print('\033[31mInfelizmente não foi desta vez!\033[m')
print('\033[33mO número sorteado foi \033[32m{}\033[m!'.format(sort))
