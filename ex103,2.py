def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome}, fez {gols} gols no campeonato!')


# programa principal
jogador = str(input('Nome do Jogador: ')).capitalize()
gol = str(input('Gols do jogador: ' )).strip()
if gol.isnumeric(): #para ver se o valor é numerico
    gol = int(gol) #caso seja numero recebe valor "inteiro"
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome=jogador, gols=gol)

