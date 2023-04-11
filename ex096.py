#exercicio definição de funções, calculo área de terrenos.


def area(l, c):
    print(f'A área de um terreno [{l:.2f}m x {c:.2f}m] é de {l*c:.2f}m².')
print('Controle de Terrenos')
print('-' * 20)
area(float(input('Largura(m): ')), float(input('Comprimento(m): ')))
