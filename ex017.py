#CALCULANDO A HIPOTENUSA DO TRIÂNGULO RETÂNGULO


print('CALCULANDO A HIPOTENUSA DO TRIÂNGULO RETÂNGULO')
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca) # Mesma coisa que o teorema de Pitágoras, hi = sqrt(x**2 + y**2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
