#encontrado as vogais nas palavras


palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
