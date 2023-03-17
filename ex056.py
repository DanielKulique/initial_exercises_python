#Trabalhando com listas


lista_idade = []
lista_nome = []
cont = 0
maior = 0
menor = 0
velho = ''
novo = ''
for p in range(1, 5):
    print(f'-----{p}ª PESSOA-----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sex = str(input(f'Sexo [M/F]: ')).upper().strip()
    lista_idade.append(idade)
    if sex == 'M':
        idadeh = idade
        if p == 1:
            maior = idadeh
            velho = nome
            menor = idadeh
            novo = nome
        else:
            if idadeh > maior:
                maior = idadeh
                velho = nome
            if idadeh < menor:
                menor = idadeh
                novo = nome
    elif sex == 'F':
        idadem = idade
        if idadem < 20:
            cont = cont + 1
    else:
        print('gênero não encontrado')
print(f'A média das idades 4 idades é {sum(lista_idade)/4} anos')
print(f'O homem mais velho é o {velho} com {maior} anos!')
print(f'{cont} mulhere(s) tem menos que 20 anos!')
