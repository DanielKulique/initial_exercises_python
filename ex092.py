#calculo de aposentadoria


from datetime import date
anoatual = date.today().year # verifica o ano atual da máquina
ficha = dict()
ficha['Nome'] = str(input('Nome: ')).capitalize()
anasc = int(input('Ano de Nascimento: '))
ficha['Idade'] = (anoatual - anasc)
while True:
    CTPS = int(input('Carteira de Trabalho (0 se não tem): '))
    if CTPS == 0:
        ficha['CTPS'] = '0'
        break
    else:
        ficha['CTPS'] = CTPS
        contrato = int(input('Ano de Contratação: '))
        contribuicao = (contrato + 35) - anasc
        ficha['Aposentadoria'] = contribuicao
        ficha['Salário R$'] = float(input('Salário: R$'))
        break
print('-='*30)
for k, v in ficha.items():
    print(f'{k} tem o valor de {v} anos')
