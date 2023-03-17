#Analise de números


from time import sleep
i = 'inicio'
print('\033[33mANALISE DE NÚMEROS E CÁLCULOS')
n1 = float(input('1ª número: '))
n2 = float(input('2ª número: '))
while i == 'inicio':
    print('\033[32m[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    acao = int(input('\033[33mDigite a ação escolhida: '))
    if acao == 1:
        print(f'\033[33mA soma de {n1} + {n2} equivale: {n1 + n2}')
    elif acao == 2:
        print(f'\033[33mA multiplicação de {n1} x {n2} equivale: {n1 * n2}')
    elif acao == 3:
        if n1 == n2:
            print('Os dois valores são equivalentes')
        elif n2 > n1:
            print(f'\033[33mO Maior valor digitado é {n2}')
        else:
            print(f'\033[33mO Maior valor digitado é {n1}')
    elif acao == 4:
        #i = 'inicio'
        print('\033[31mReiniciando...')
        sleep(0.5)
        n1 = float(input('\033[33m1ª número: '))
        n2 = float(input('2ª número: '))
    elif acao == 5:
        i = 'parar'
        print('\033[31mDesligando...')
        sleep(1)
    else:
        print('\033[31mOpção inválida. Tente novamente!')
    print('\033[31m-='*20)
print('\033[32mFim do programa!')
