#tratamento de strings, se há "SANTO" no nome da cidade


#OUTRA FORMA
cid = str(input('Em que cidade você nasceu?' )).strip()
print(cid[:5].upper() == 'SANTO')
