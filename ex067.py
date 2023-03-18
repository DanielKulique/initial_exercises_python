#tabuada do número inserido (com estrutura de repetição)


from time import sleep
while True:
    print('-' * 10, '\033[33mTabuada\033[0m', '-' * 10)
    n = int(input('Digite um número: '))
    if n < 0:
        print('\033[31mEncerrando a calculadora...')
        sleep(1)
        break
    cont = 1
    while cont <= 10:
        print(f'{cont:2} X {n} = {n*cont}')
        sleep(0.3)
        cont += 1
