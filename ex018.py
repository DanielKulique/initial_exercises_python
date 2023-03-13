#Retornando sen, cos e tan de um ângulo qualquer


print('Retornando sen, cos e tan de um ângulo qualquer')
ang = float(input('Digite o valor em graus do ângulo desejado: '))
import math
sen = (math.sin(math.radians(ang)))
cos = (math.cos(math.radians(ang)))
tan = (math.tan(math.radians(ang)))
print('O ângulo {} tem: \nseno de {:.2f} \ncosseno de {:.2f} \ntangente de {:.2f}' .format(ang, sen, cos, tan))
