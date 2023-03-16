#calculo massa corporal


print('\033[4m-=-'*3,'CALCULO IMC','-=-'*3, '\033[m')
peso = float(input('\033[33mDigíte o seu peso em Kilograma: '))
altura = float(input('Digíte a sua altura em metros: '))
imc = peso / (altura ** 2) #Kg/m2
if imc < 18.5:
    print('\033[31mAbaixo do peso!')
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal!')
elif 25 <= imc < 30:
    print('\033[33mSobre peso!')
elif 30 <= imc < 40:
    print('\033[31mObesidade!')
else:
    print('\033[31mObesidade mórbida!')
print(f'IMC = {imc:.2f}')
