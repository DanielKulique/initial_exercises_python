#alistamento militar


from datetime import date
ano = date.today().year #ano atual do aparelho
sexo = str(input('\033[33mDigite seu sexo: ')).strip()
if sexo.upper() == 'HOMEM':
    nascimento = int(input('\033[33mDigíte seu ano de nascimento: '))
    idade = ano - nascimento
    if idade == 17:
        print('\033[4;49;33mAtenção você deve se prepapar para o alistamento obrigatório!')
    elif idade == 18:
        print('\033[4;49;33mVocê já deve ter pelo menos jurado a bandeira!')
    elif idade < 17:
        anosf = 18 - idade
        print(f'\033[32mfaltam {anosf} ano(s) para seu alistamento obrigatório!')
    elif 19 <= idade <= 23:
        anosf2 = 24 - idade
        print(f'\033[32mCaso foi dispensado, você ainda pode servir ao exército e faltam {anosf2} ano(s) para decidir!')
    else:
        print(f'\033[31mVocê está isento do serviço militar!')
elif sexo.upper() == 'MULHER':
    print('\033[32mVocê não precisa fazer alistamento!')
else:
    print('\033[31mSexo não identificado, por favor tente novamente.')












