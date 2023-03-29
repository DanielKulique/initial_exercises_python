#calculo de média e tabela


ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    ficha.append([nome, [nota1, nota2], media])
    while True:
        action = str(input('Deseja continuar?[S/N]: '))[0]
        if action in 'SsNn':
            break
        else:
            print('Opção não identificada... ', end='')
    if action in 'Nn':
        break
print('-='*30)
print(f'{"nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, est in enumerate(ficha): #est = estudante
    print(f'{i:<4}{est[0].capitalize():<10}{est[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual estudante? (999 interrompe): ')) #opc = opção
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0].capitalize()} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
