#estrutura de repetição


print('\033[33m-=-'*14)
print('Números impares de 0 a 500 multiplos de 3')
print('-=-'*14, '\033[32m')
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #contador soma a quantidade de valores
        s = s + c #acumulador soma um valor
print(f'A soma dos {cont} valores é equivalente a {s}')
