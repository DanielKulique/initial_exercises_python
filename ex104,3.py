#definindo função para ler números inteiros


def leiaint(msg): #função leia recebe mensagem (Digite um número)
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
