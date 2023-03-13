#quebra de número


print('-'*7,'Quebra de número', '-'*7)
from math import trunc
d = float(input('Digite seu valor decimal desejado: '))
i = trunc(d)
print('O valor decimal {} foi convertido ao valor inteiro {} com sucesso!'.format(d, i))
