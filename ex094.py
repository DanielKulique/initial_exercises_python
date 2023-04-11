#ex. listas e dicionários. cadastro de pessoas(idade, sexo, nome). verificação de dados.


pessoa = dict()
grupo = list()
while True:
    pessoa['NOME'] = str(input('Nome: ')).capitalize()
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
        if sexo in 'M':
            pessoa['SEXO'] = 'Masculino'
            break
        elif sexo in 'F':
            pessoa['SEXO'] = 'Feminino'
            break
        else:
            print('Sexo não identificado...', end='')
    pessoa["IDADE"] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        action = str(input('Deseja continuar?: [S/N]: '))[0]
        if action in 'SsNn':
            break
        else:
            print('Ação não identificada... ')
    if action in 'Nn':
        break
print(grupo)
print('-='*40)
#A
print(f'O grupo tem {len(grupo)} pessoas.')
#b
soma = 0
print(f'-A média de idade é de ', end='')
for p in grupo:
    soma += p['IDADE']
print(f'{soma / len(grupo):.2f} anos')
print('-As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['SEXO'] in 'Feminino':
        print(f'{p["NOME"]}', end=" ")
print('\n-Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['IDADE'] > (soma / (len(grupo))):
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('')
print('')
print('<< ENCERRADO >>')
