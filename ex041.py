#categoria do atléta por idade


from datetime import date
ano = date.today().year #retorna a data atual da máquina
idade = int(input('\033[33mDigite em qual ano o atleta nasceu: '))
atual = ano - idade #calculo idade do atleta
if atual <= 9:
    print(f'\033[32mCom {atual} anos sua categoria é a MIRIM!')
elif atual <= 14:
    print(f'\033[32mCom {atual} anos sua categoria é a INFANTIL!')
elif atual <= 19:
    print(f'\033[32mCom {atual} anos sua categoria é a JUNIOR!')
elif atual <= 20:
    print(f'\033[32mCom {atual} anos sua categoria é a SÊNIOR!')
else:
    print(f'\033[31mA categoria com {atual} anos é a de MASTER!')
