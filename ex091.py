#randomização de números e ranking de jogadores


from random import randint
from time import sleep
from operator import itemgetter
sorteios = {}
ranking = dict()
print('Valores sorteados:')
for r in range(1, 5):
    sorteios[f'jogador({r})'] = (randint(1, 6))
for k, v in sorteios.items():
    print(f'O {k} tirou {v}')
    sleep(0.8)
ranking = sorted(sorteios.items(), key=itemgetter(1), reverse=True)
print('============Ranking dos Jogadores============')
for e, r in enumerate(ranking):
    print(f'O {e+1}º lugar ficou para {r[0]} com {r[1]} pontos!')
