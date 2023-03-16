#sistema de pagamento


vp = float(input('\033[33mDigíte o valor do produto em R$: '))  # vp == valor produto
pag = int(input('\033[4;33mQual a forma de pagamento?\033[0;33m \n'  # pag == tipo do pagamento
                '[1] Vista no dinheiro/cheque com 10% de desconto; \n'
                '[2] À vista no cartão com 5% de desconto; \n'
                '[3] Até 2x sem juros; \n'
                '[4] 3x ou mais no catão com 20% de juros. \n'
                '\033[32mDigite aqui:'))
if pag == 1:
    vp = vp - (vp * 0.10)  # com 10% de desconto
    print(f'\033[32mValor do produto ficará R${vp} com o desconto de 10%!')
elif pag == 2:
    vp = vp - (vp * 0.05)  # com 5% de desconto
    print(f'\033[32mValor do produto ficará R${vp} com o desconto de 5%!')
elif pag == 3:
    vp = vp / 2
    print(f'\033[32mValor do produto será R${vp} ao mês por 2 meses sem juros!')
elif pag == 4:
    vez = int(input('\033[33mEm quantas vezes desaja parcelar?'))  # vez == vezes da parcela
    if vez >= 3:
        vp = ((vp * 0.20) + vp) / vez
        total = vp * vez
        print(f'\033[32mEm {vez} parcelas o produto custará R${vp} por mês com 20% de juros ao todo!'
              f' Custando ao final um total de R${total}!')
    else:
        print(
            f'\033[31mA parcela digítada é menor que 3x, por favor escolha outra opção de pagamento!')  # caso o usuario digite uma parcela menor que 3X
