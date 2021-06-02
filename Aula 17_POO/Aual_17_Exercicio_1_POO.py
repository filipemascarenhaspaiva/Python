'''1. Utilizando os conceitos de Orientação a Objetos (OO) vistos
na aula anterior, crie um lançador de dados e moedas em que o
usuário deve escolher o objeto a ser lançado. Não esqueça que os
lançamentos são feitos de forma randômica.'''

import random


class Moeda:

    def __init__(self):
        self.lado = random.randint(1, 2)

    def lancar(self):
        if self.lado == 1:
            print('Deu cara')
        if self.lado == 2:
            print('Deu coroa')


class Dado:

    def __init__(self):
        self.face = random.randint(1, 6)

    def rolar(self):
        if self.face == 1:
            print('O dado caiu com o lado de numero 1 para cima')
        if self.face == 2:
            print('O dado caiu com o lado de numero 2 para cima')
        if self.face == 3:
            print('O dado caiu com o lado de numero 3 para cima')
        if self.face == 4:
            print('O dado caiu com o lado de numero 4 para cima')
        if self.face == 5:
            print('O dado caiu com o lado de numero 5 para cima')
        if self.face == 6:
            print('O dado caiu com o lado de numero 6 para cima')


moeda = Moeda()
dado = Dado()
print('                    Jogo da sorte')
print()
print('1. Moeda')
print('2. Dado')
print()
escolha = input('Escolha entre jogar com a moeda ou com o dado: ')

if escolha == '1':
    moeda.lancar()
elif escolha == '2':
    dado.rolar()
else:
    print("Opção invalida")
