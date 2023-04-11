#definição de função: contagem progressiva e regressiva


from time import sleep


def contagem(ini, fim, passo):
    if passo == 0:
        print(f'Valor 0 é inválido, passo recebe "1"!')
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    while ini < fim:
        print(ini, end=' ')
        sleep(0.5)
        ini += passo
    while ini >= fim:
        print(ini, end=' ')
        sleep(0.5)
        ini -= passo
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contagem(ini=(int(input('Inicio: '))), fim=(int(input('Fim: '))), passo=(int(input('Passo: '))))
