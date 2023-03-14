#tratamento de strings


frase = str(input('Digíte uma frase: ')).strip()
fraseM = frase.upper()
print('A letra "A" aparece {} vezes na frase.'.format(fraseM.count('A')))
fraseD = fraseM.split()
fraseMJ = (''.join(fraseD))
print('É encontrada a letra "A" pela primera vez no {}° caractere da frase.'.format((fraseMJ.find('A', 0)+1)))
print('É encontrada a letra "A" pela última vez no {}° caractere da frase.'.format((fraseMJ.rfind('A')+1)))
