#randomizando em tuplas

from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
#print(f'os números sorteados são: {tupla}\nO maior entre eles é {max(tupla)}\nO menor {min(tupla)}')
print('Os valores sorteados foram: ', end='')
maior = 0
menor = 10
for n in tupla:
    print(f'{n} ', end='')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('\n-------------------------')
print(f'O maior valor foi: {maior}\n'
      f'O menor valor foi: {menor}')
