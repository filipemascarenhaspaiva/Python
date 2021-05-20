'''2. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feito em cada partida. No final tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato'''

nome = input('Nome do jogador: ')
partidas = int(input('Quantas partidas ele jogou: '))
contador = 0
gols = []
for i in range(1, partidas+1):
    contador += 1
    qta_gols = int(input(f'Quantos gols foram feitos na partida {contador}: '))
    gols.append(qta_gols)
aproveitamento = {'Jogador': nome,
                  'Partidas Jogadas': partidas, 'Gols no Campeonato': sum(gols)}
print(aproveitamento)
