'''Exercício 3 - Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. 

Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)

5 - Voto Nulo

6 - Voto em Branco

Faça um programa que calcule e mostre:

-O total de votos para cada candidato;

-O total de votos nulos;

-O total de votos em branco;

-A percentagem de votos nulos sobre o total de votos;

-A percentagem de votos em branco sobre o total de votos. 

-Para finalizar o conjunto de votos tem-se o valor zero.'''

print('Guia de votação')
print('\nCandidato  Numero')
print('Rushi | 1')
print('Kenay | 2')
print('Nelia | 3')
print('Yanna | 4')
print('Voto Nulo | 5')
print('Voto Branco | 6')
print('\n Digite 0 para encerrar a votação e imprimir as estatisticas')
Rushi = []
Kenay = []
Nelia = []
Yanna = []
Voto_Nulo = []
Voto_Branco = []

voto = int(input('\nVote inserindo o numero do candidato: '))
while voto == 1:
    Rushi.append(voto)
    voto = int(input('\nVote inserindo o numero do candidato: '))
    if voto == 0:
        break
while voto == 2:
    Kenay.append(voto)
    voto = int(input('\nVote inserindo o numero do candidato: '))
    if voto == 0:
        break
while voto == 3:
    Nelia.append(voto)
    voto = int(input('\nVote inserindo o numero do candidato: '))
    if voto == 0:
        break
while voto == 4:
    Yanna.append(voto)
    voto = int(input('\nVote inserindo o numero do candidato: '))
    if voto == 0:
        break
while voto == 5:
    Voto_Nulo.append(voto)
    voto = int(input('\nVote inserindo o numero do candidato: '))
    if voto == 0:
        break
while voto == 6:
    Voto_Branco.append(voto)
    voto = int(input('\nVote inserindo o numero do candidato: '))
    if voto == 0:
        break
print('\nEstatisticas das eleições')
print(f'\nCandidato Ruchi teve {len(Rushi)} votos')
print(f'\nCandidato Kenay teve {len(Kenay)} votos')
print(f'\nCandidata Nelia teve {len(Nelia)} votos')
print(f'\nCandidato Yanna teve {len(Yanna)} votos')
print(f'\nO total de votos nulos foi de {len(Voto_Nulo)} votos')
print(f'\nO total de votos em Branco foram {len(Voto_Branco)} votos')

total_votos = len(Rushi) + len(Kenay) + len(Nelia) + len(Yanna)
percentual_votos_nulos = (len(Voto_Nulo) * 100) / total_votos
percentual_votos_brancos = (len(Voto_Branco) * 100) / total_votos

if len(Rushi) == 0:
    print('O candidato Ruchi teve 0 votos')
if len(Kenay) == 0:
    print('O candidato Kenay teve 0 votos')
if len(Nelia) == 0:
    print('A candidata Nelia teve 0 votos')
if len(Yanna) == 0:
    print('A candidata Yanna teve 0 votos')
if len(Voto_Nulo) == 0:
    print('Tivemos 0 votos anulados')
if len(Voto_Branco) == 0:
    print('Tivemos 0 votos em branco')
