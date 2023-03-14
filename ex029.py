#radar de velocidade


vel = float(input('Velocidade do carro apontada pelo radar em Km/h?: '))
cus = (vel-80)*7
if vel > 80:
    print('O limite de velocidade foi ultrapassado! \nO valor da multa a ser pago é R${:.2f}.'.format(cus))
else:
    print('O veiculo está dentro do limite permitido!')
