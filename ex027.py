#tratamento de strings


print('\033[1;33m-=-=-VERIFICADOR DE NOME-=-=-\033[m')
n = str(input('\033[4;33mDigíte seu nome completo:\033[m ')).strip()
nome = n.split()
print('\033[32mMuito prazer em te conhecer\033[m!')
print(f'\033[4mSeu primeiro nome é {nome[0]}!\033[m')
print(f'\033[4mSeu último nome é {nome[len(nome)-1]}!\033[m') # da lista 'nome' [ler( os nomes) - 1)] = mostrar o último da lista.
