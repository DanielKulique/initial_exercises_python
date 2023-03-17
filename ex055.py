#Maior e menor valor da lista


s = 0
s2 = 0
lista_simples = []
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    lista_simples.append(peso)
print(f'Entre os 6 pesos digitados, o maior é {max(lista_simples):.2f} e o menor foi {min(lista_simples):.2f}!')
