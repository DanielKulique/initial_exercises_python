#criando um jogo


print('\033[33m', '-=-'*3, 'JOKENPÔ', '-=-'*3, '\033[m')
esc = str(input('\033[4;31mEscolha pedra, papel ou tessoura:\033[m ')).upper().strip()
import random
sort = random.randint(1, 3) #(pedra == 1), (papel == 2), (tessoura == 3)
###################
if sort == 1:
    comp = 'pedra'
elif sort == 2:
    comp = 'papel'
else:
    comp = 'tessoura'
###################
if esc == 'PEDRA' and comp == 'pedra' \
        or esc == 'PAPEL' and comp == 'papel' \
        or esc == 'TESSOURA' and comp == 'tessoura':
    print(f'\033[34m{comp.capitalize()} com {esc.capitalize()} é empate, jogue novamente!')
elif esc == 'PEDRA' and comp == 'tessoura' \
        or esc == 'PAPEL' and comp == 'pedra' \
        or esc == 'TESSOURA' and comp == 'papel':
    print(f'\033[32m{esc.upper()} ganha de {comp.upper()}, você ganhou!!!')
else:
    print(f'\033[31m{comp.upper()} ganha de {esc.upper()}, infelizmente você perdeu!')
