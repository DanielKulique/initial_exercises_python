#validador de expressões


expr = str(input('Digite sua expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('Não válida')
else:
    print('Válida')
print(pilha)
