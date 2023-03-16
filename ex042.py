#se as medidas do lado formam um triangulo ou não


a = float(input('\033[33mDigíte o valor do primeiro lado: '))
b = float(input('Digíte o valor do segundo lado: '))
c = float(input('Digíte o valor do terceiro lado: \033[m'))
if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+c):
    print(f'\033[32mAs medidas {a}, {b} e {c} formam um triângulo!')
    if a == b and a == c and b == c:
        print('Todos os lados tem a mesma medidas, ou seja, o trinângulo é EQUILÁTERO!')
    elif a == b or b == c or a == c:
        print('Dois lados são iguais! O triãngulo é ISÓSCELES!')
    else:
        print('Todos os lados são diferentes! O triângulo é ESCALENO!.')
else:
    print('\033[31mAs medidas dos lados não formam um triângulo!')
