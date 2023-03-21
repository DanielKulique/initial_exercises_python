#utilizando tuplas


times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
         'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('\033[34m','='*270)
print('\033[33m Lista dos times =', times)
print('\033[34m','='*270)
print('\033[32m Primeiros 5 colocados=', times[0:5])
print('\033[34m='*100)
print('\033[31m Últimos 4 colocados=', times[-4:]) # ou times[16:]
print('\033[34m','='*270)
print('\033[33m Lista em ordem alfabética dos times:', sorted(times))
print('\033[34m','='*270)
print('\033[32m O Corinthians está na {}ª posição!'.format(times.index('Corinthians')+1))
