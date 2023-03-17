#advinhação de número com randomização


from random import randint
from time import sleep
r = 'rep'
cont = 1
print('\033[33mVou pensar em um número de 1 a 10, tente adivinhar!')
while r == 'rep':
    sort = randint(1, 10)
    esc = int(input('Digíte o número: '))
    print('\033[33mprocessando...')
    sleep(1)
    if sort != esc:
        print('\033[31mErrouuu.. tente novamente!')
        cont += 1
    else:
        print(f'\033[32mParabéns, após {cont} tentativas você venceu!')
        r = ''
