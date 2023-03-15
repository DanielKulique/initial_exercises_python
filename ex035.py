#as 3 medidas formam um triângulo?


a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do teceiro lado: '))
if abs(b-c) < a < (b+c):
    if abs(a-c) < b < (a + c):
        if abs(a-b) < c < (a + c):
            print('As medidas formam um triângulo!')
        else:
            print('As medidas não formam um triângulo!')
    else:
        print('As medidas não formam um triângulo!')
else:
    print('As medidas não formam um triângulo!')
