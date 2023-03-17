#verificação de idade com estrutura de controle


from datetime import date
aatual = date.today().year
cont = 0
contp = 0
for c in range(1, 8):
    n = int(input('Digite sua data de nascimento: '))
    contp += 1
    if (aatual - n) < 18:
        cont = cont + 1
print(f' Das {contp} pessoas verificadas, {cont} são menores de idade e {abs(contp-cont)} são maiores de idade')
