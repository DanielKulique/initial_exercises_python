#calculo média e situação do estudante


estudante = dict()
estudante['Nome'] = (str(input('Nome: '))).capitalize()
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
estudante['Média'] = ((nota1 + nota2) / 2)
if estudante['Média'] <= 4.9:
    estudante['Situação'] = 'Reprovado'
elif 4.9 < estudante['Média'] <= 5.9:
    estudante['Situação'] = 'pendente'
else:
    estudante['Situação'] = 'Aprovado'
ficha = [estudante]
print('-='*30)
#print(f'Média de {ficha[0]["nome"]} é igual a {ficha[0]["média"]:.1f}, ou seja, está {ficha[0]["Situação"].upper()}!')
for est in ficha:
    for k, v in est.items():
        print(f'{k} é igual a {v}')
