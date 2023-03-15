#maior e menor valor digitado


a = float(input('Digite um número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
#menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
