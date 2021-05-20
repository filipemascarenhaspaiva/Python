'''Crie um programa em que 4 jogadores, joguem um dado de
20 faces e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.'''
from operator import itemgetter
import random
pontos = {}
for i in range(1, 5):
    pontos[i] = random.randint(1, 20)
sorted(pontos.items(), key=itemgetter(1))
max_key = max(pontos.items(), key=itemgetter(1))[0]
print('O jogador 1 fez ', pontos[1], 'Pontos')
print('O jogador 2 fez ', pontos[2], 'Pontos')
print('O jogador 3 fez ', pontos[3], 'Pontos')
print('O jogador 4 fez ', pontos[4], 'Pontos')
print('O jogador', max_key,
      'teve a maior pontuação, um valor de', pontos[max_key], 'pontos, portanto ele é o vencedor')
