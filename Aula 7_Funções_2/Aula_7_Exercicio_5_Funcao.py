'''Exercicio 5 Faça um programa que tenha uma função 
chamada ficha(), que receba dois parâmetros: o nome 
de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do 
jogador, mesmo que algum dado não tenha sido 
informado corretamente.'''


def ficha(nome_jogador=str('jorge'), gol=10):
    print(f'o jogador {nome_jogador} fez {gol} gols')


ficha()
