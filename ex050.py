#estrutura de repetição


s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite seu número: '))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print(f'soma dos {cont} números pares digitados é equivalente a {s}!')
