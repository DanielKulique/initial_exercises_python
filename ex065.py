#maior e menor número digitado com estrutura de controle


i = ''
cont = 0
list_num = []
while i == '':
    n = int(input('\033[33mDigite o número: '))
    cont += 1
    list_num.append(n)
    acao = str(input('\033[31mDeseja continuar?[S/N]: ')).upper().strip()
    if acao == 'S':
        continue
    else:
        break
soma = sum(list_num)
print(cont)
print(f'\033[32mO maior valor digitado foi [{max(list_num)}], o menor [{min(list_num)}] e a média entre eles é [{soma/cont:.2f}]')
