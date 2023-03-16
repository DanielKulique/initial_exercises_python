#estrutura de repetição


print('\033[33m-=-'*5)
print(str('TABUADA').center(15))
print('\033[33m-=-'*5)
n = int(input('Digite o número desejado: '))
for c in range(1, 11):
    t = c * n
    print(f'\033[32m {n} x {c:2} = {t}')
