from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.') #parametro 1, entrada do preço
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.') #parametro 2 (True ou False), chamada da formatação.
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.')
print(f'Reduzinho 13%, temos {moeda.diminuir(p, 13, True)}.')