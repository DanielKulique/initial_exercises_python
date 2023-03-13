#calculo de área


print('Área da parede e quantidade de tinta nescessária para pintá-la')
l = int(input('Digite a largura em metros da parede:')) #metros
h = int(input('Digite a altura em metros da parede:')) #metros
A = l * h
L = A / 2
print('A área da parede é {:.2f}m^2, sendo preciso {:.2f}L de tinta para pintá-la'. format(A, L))
