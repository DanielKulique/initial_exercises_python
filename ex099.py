#ex. definições de funções, analisando parâmetros


from time import sleep
def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    mai = 0
    for e, n  in enumerate(num):
        if e == 0:
            mai = n
        else:
            if mai <= n:
                mai = n
        print(n, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}') # OU USAR MAX(NUM)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
