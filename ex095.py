#partidas jogadas e gols feitos.


ficha = dict()
grupo = list()
while True:
    print('-' * 34)
    ficha['NOME'] = str(input('Nome do jogador: ')).capitalize()
    jogos = int(input(f'Quantas partidas {ficha["NOME"]} jogou?: '))
    gols = list()
    for r in range(0, jogos):
        gols.append(int(input(f'Quantos gols na partida {r}?: '))) #gols feitos
    ficha['GOLS'] = gols #tirei str, agr recebe valor numerico
    ficha['TOTAL'] = sum(gols)
    grupo.append(ficha.copy())
    while True:
        action = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if action in 'SN':
            break
    if action in 'N':
        break
print('-='*30)
print(f'{"cod":<4}{"nome":<20}{"gols":<20}{"total":<20}')
for e, j in enumerate(grupo): # j = jogador in grupo
    print(f'{e:<4}{j["NOME"]:<20}{str(j["GOLS"]):<20}{j["TOTAL"]:<20}')
print('-='*30)
action = 0
while True:
    while True:
        action = int(input('Mostrar dado de qual jogador? '))
        if 0 <= action < (len(grupo)) or action == 999:
            break
        else:
            print(f'ERRO! Não existe jogador com código {action}! Tente novamente...')
    if action == 999:
        break
    print('-' * 34)
    print(f'-- LEVANTAMENTO DO JOGADOR {grupo[action]["NOME"]}')
    for e, j in enumerate(grupo[action]["GOLS"]): # j = jogador in grupo // (LISTA[DICIONÁRIO(LISTA)])
        print(f'Na jogo {e} fez {j} gols.')
    print('-' * 34)
print('<< VOLTE SEMPRE >>')
