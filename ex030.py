#verificação se o número é impar ou par


num = int(input('Digíte um número qualquer: '))
resultado = num % 2 #resto da divisão de número por "2"
if resultado == 0:  #todos números pares não apresenta resto de divisão quando dividido por 2, já os impares sim!
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))
