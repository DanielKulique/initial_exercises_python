#ex. listas e dicionários. jogador, gols e total de partidas.


ficha = dict() #jogador
gols = list()  #partidas
ficha['Nome'] = str(input('Nome do jogador: ')).capitalize()
jogos = int(input(f'Quantas partidas {ficha["Nome"]} jogou?:' ))
for r in (range(0, jogos)):
    gols.append(int(input(f'Quantos gols na partida {r}?: '))) #gols feitos
print('-='*30)
ficha['gols'] = gols[:]
ficha['total'] = sum(gols)
print(ficha)
print('-='*30)
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O jogador {ficha["Nome"]} jogou {len(ficha["gols"])} partidas')
for e, g in enumerate(ficha["gols"]):
    print(f'    => Na partida {e}, fez {g} gols.')
print(f'Foi um total de {ficha["total"]} gols.')
