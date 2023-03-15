#utilização e if, elif e else.


a = int(input('\033[33mDigite o valor desejado: '))
b = int(input('Digite o segundo valor desejado: \033[m'))
if a > b:
    print('\033[32mO primeiro valor é maior!')
elif b > a:
    print('\033[32mO segundo valor é maior!')
else:
    print('\033[31mNão há valor maior, os dois são equivalentes!')
