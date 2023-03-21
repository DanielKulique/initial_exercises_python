#utilizando tuplas


contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 a 20: '))
        if -1 < n < 21:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {contagem[n]}!')
    acao = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if acao == 'N':
        from time import sleep
        print('Encerrando...')
        sleep(1)
        break
