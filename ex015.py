#calculo valor do aluguel de um carro qualquer


print('Aluguel de carros')
km = int(input('Digite a quantidade de Km rodados com o carro:'))
d = float(input('Digite a quantidade de dias de locação do carro:'))
v = (km * 0.15) + (d * 60)
print('O valor total a ser pago pelo aluguel é de R${:.2f}.'.format(v))
