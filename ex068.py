#Jogo de números impares e pares (com estruta de repetição)


from random import randint
cont = 0
while True:
    comp = randint(0, 11)
    while True:
        esc = str(input('\033[33mImpar[I] ou Par[P]?')).strip().upper()
        if esc == 'I' or esc == 'P':
            break
    player = int(input('\033[33mDigite seu número: '))
    soma = comp + player
    resul = soma % 2
    if resul == 0 and esc == 'P':
        print(f'\033[32mPC jogou {comp}, {soma} é PAR, você Ganhou!')
    elif resul != 0 and esc == 'I':
        print(f'\033[32mPC jogou {comp}, {soma} é IMPAR, você Ganhou!')
    else:
        if esc == 'I':
            esc = 'IMPAR'
        elif esc == 'P':
            esc = 'PAR'
        if resul == 0:
            resp = 'PAR'
        else:
            resp = "IMPAR"
        print(f'\033[31mPC jogou {comp}, {soma} é {resp}. Após {cont} vitórias, você escolheu {esc} e perdeu para o computador!')
        break
    cont += 1
