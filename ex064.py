#soma dos números digitados


i = ''
list_num = []
cont = 1
while i == '':
    n = int(input('Digite um número [999 para]: '))
    if n == 999:
        break
    list_num.append(n)
    cont += 1
print(f'\033[33mDos {cont} número digitados, a soma deles equivalem a {sum(list_num)}!')
