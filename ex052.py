#números primos com estrutura de controle


print('\033[33mO número é primo? ')
n = int(input('Digíte o número desejado: \033[32m'))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
    #print(n / c)
    if n % c == 0:
        cont = cont + 1
        #print(c)
#print('-----')
print('\n\033[33m-----------------------------')
if cont == 2:
    print(f'\033[32mO número {n} é primo!')
else:
    print(f'\033[31mO número {n} não é primo!')
#print(cont)
