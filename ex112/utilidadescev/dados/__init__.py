def leiadinheiro(msg):
    valido = False
    entrada = ''
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada in '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido!\033[0m')
        else:
            valido = True
    return float(entrada)


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




