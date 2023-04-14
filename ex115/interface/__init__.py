c = ('\033[m',          # 0 - sem cores
     '\033[31m',   # 1 - vermelho
     '\033[32m',   # 2 - verde
     '\033[33m',   # 3 - amarelho
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;95m')      # 6 - branco


def leiaint(msg):
    while True:
        try:
            verif = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[33mO usuário deciciu não informar o número.')
            return 0
        else:
            return verif


def linha(tam = 42):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(f'{txt:^42}')
    linha()


def menu(lista, cor = 0):
    print(c[cor], end='')
    for item in lista:
        print(item)
    print(c[0], end='')
    linha()
    while True:
        option = leiaint(f'{c[2]}Sua Opção: {c[0]}')
        if 0 < option <= (len(lista)):
            return option                          #option retorna uma resposta do usuário
        else:
            print(f'{c[1]}Digite um número entre 1 e {len(lista)}')
            continue
