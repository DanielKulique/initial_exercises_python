#estrutura de controle


pal = str(input('Digite a palavra desejada: ')).strip()
palM = ''.join(pal.upper().split())
tl = len(palM)
iv = palM[::-1]
cont = 0
for c in range(0, tl):
    if palM[c] == iv[c]:
        cont = cont + 1
if cont == tl:
    print(f'A palavra/frase "{pal}" palíndromo')
else:
    print('frase normal')
