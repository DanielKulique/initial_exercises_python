def voto(nasc):
    from datetime import date
    anoA = date.today().year
    idade = anoA - nasc
    if idade < 18:
        nasc = f'Com {idade} anos ainda NÃO é possivel votar'
    if 18 <= idade <= 70:
        nasc = f'Com {idade} anos seu voto é OBRIGATÓRIO'
    if idade > 65:
        nasc = f'Com {idade} anos seu voto é OPCIONAL'
    print(nasc)


print('----------------------------')
nascimento = int(input('Ano de nascimento: '))
voto(nascimento)