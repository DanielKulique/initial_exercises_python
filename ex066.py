#soma dos números digitados com estrutura de repetição


cont = soma = 0
while True:
    n = int(input('Digite um número [999 stop]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'\033[33mA soma dos {cont} números digitados equivalem a {soma}')
