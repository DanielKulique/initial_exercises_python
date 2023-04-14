#utilizando modularização e def de funções


from ex115.interface import *


def arquivo(nome = 'texto.txt', tipo = 'a'):
    arq = open(nome, tipo)
    return arq


def lerarquivo(nome):
    global a
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>17} anos')
    finally:
        a.close()


def cadastrar(arq='cadastro.txt', nome='desconhecido', idade=0):
    try:
        lista = open(arq, 'a')
    except:
        print(f'Ocorreu um erro no arquivo {arq}')
    else:
        try:
            lista.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            lista.close()


def escrever(nome='cadastros.txt', parametro='a', txt=''):
    pasta = open(nome, parametro)
    pasta.write(txt)
