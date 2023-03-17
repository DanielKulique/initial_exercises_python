#fatorial de um número


n = int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)






