#utilizando modularização e def de funções


from ex112.utilidadescev import moeda
from ex112.utilidadescev import dados

p = dados.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 30)
