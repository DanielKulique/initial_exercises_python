#trabalhando com listas


valores = []
for p, r in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite o valor da posição {p}: ')))
menor = min(valores)
maior = max(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior} encontrado nas posições ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(p, end='... ')
print(f'\nO menor valor foi {menor} encontrado nas posições ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(p, end='... ')
print()
