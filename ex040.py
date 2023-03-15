#media e aprovoação de estudantes


n1 = float(input('\033[33mDigíte sua primeira nota: '))
n2 = float(input('Digíte a sua segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print(f'\033[31mInfelizmente sua média é ({med}). O diabo veio cobrar!')
elif 5 <= med <= 6.9:
    print(f'\033[33mSua média foi ({med}). Você está de Recuperação!')
else:
    print(f'\033[32mParabens você foi aprovado com média {med}!')
