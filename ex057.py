#Estrutura de repetição


r = 'rep'
while r == 'rep':
    s = str(input('Gênero [M/F]:')).upper().strip()
    if s == 'M' or s == 'F':
        r = 'para'
    if 'M' == s:
        print(f'O gênero é Masculino: ')
    if 'F' == s:
        print(f'O gênero é Feminino')
