#Dobro, triplo e raiz quadrada de um número


print('Dobro, triplo e raiz quadrada de um número')
n = int(input('Digite um número:'))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é {}, seu triplo {} e sua raiz quadrada {:.3f}.'.format(n, d, t, r))
