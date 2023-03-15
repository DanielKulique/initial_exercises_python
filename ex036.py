#possibilidade de fazer um empréstimo


vcasa = float(input('\033[33mDigíte o valor da casa desejada? '))               #valor casa
sal = float(input('\033[33mDigíte o valor do seu salário mensal: '))            #salário
anos = int(input('\033[33mDigite em quantos anos deseja quitar a casa:'))       #anos para pagar
vmensal = vcasa / (anos * 12)     #valor mensal
lmt = sal * 0.30                #limite de 30% salário
if vmensal >= lmt:
    print('\033[31minfelizmente não será possivel fazer o empréstimo!')
else:
    print('\033[32mO empréstimo é possível!')
