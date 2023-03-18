#Cadastro de pessoas


contI = 0
homens = 0
contM = 0
while True:
    print('-'*22)
    print(f' CADASTRE UMA PESSOA')
    print('-'*22)
    idade = int(input('Idade: '))
    if idade > 18:
        contI += 1
    while True:
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()
        if sexo == 'M' or sexo == 'F':
            break
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        contM += 1
    while True:
        acao = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if acao == 'S' or acao == 'N':
            break
    if acao == 'N':
        break
print('Fim do Programa')
print(f'Total de pessoas com mais de 18 anos: {contI}\n'
      f'Ao todo temos {homens} homens cadastrados\n'
      f'E temos {contM} mulheres com menos de 20 anos!')
