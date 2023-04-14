#utilizando modularização e def de funções


from ex115.interface import linha, cabeçalho, menu
from ex115.arquivo import arquivo, lerarquivo, cadastrar

try:
    arquivo('cadastro.txt', 'x')
    print('Arquivo criado com sucesso!')
except:
    print('Arquivo já existente!')

cabeçalho('MENU PRINCIPAL')

while True:
    reposta = menu(['1 - Ver As Pessoas Cadastradas',
                    '2 - Cadastrar Nova Pessoa',
                    '3 - Sair do Sistema'], cor = 3)
    if reposta == 1:
        lerarquivo('cadastro.txt')
        print()
        linha()
    elif reposta == 2:
        cabeçalho('NOVO CADASTRO')
        nom = str(input('Nome: ')).capitalize()
        idad = int(input('Idade: '))
        cadastrar(arq='cadastro.txt', nome=nom, idade=idad)
    elif reposta == 3:
        cabeçalho('Saindo do sistema!')
        break
