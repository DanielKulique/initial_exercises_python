#formatação de strings


nome = str(input('Digíte seu nome: ')).strip()                                          #entrada do nome
nomeM = nome.upper()                                                           # nomeM (nome maiúsculo)
nomem = nome.lower()                                                           # nomem (nome minúsculo)
print('Nome em letras maiúsculas: {}' .format(nomeM))                          # mostrar nomeM
print('Nome em letras minúsculas: {}' .format(nomem))                          # mostrar nomem
print('Total de letras na frase: {}'.format(len(''.join(nome.split()))))       # len (comprimento da frase), join (junta a frase),
dnome = nome.split()                                                           #dividir nome em listas
print('O primeiro nome tem {} letras'.format(len((dnome[0]))))                 #indicar quantidades de caracteres na primeira palavra da lista

