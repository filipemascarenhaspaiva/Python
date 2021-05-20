'''Faça um jogo da forca. O programa terá uma lista de palavras
lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador
poderá errar 6 vezes antes de ser enforcado.'''

import random  # importa o módulo random
palavras = ("Abacaxi bola peixe gato morango chiclete")
palavras = palavras.split(" ")
# pega um número aleatoriamente entre 0 e número de palavras
uma_palavra = palavras[random.randrange(0, len(palavras))]
palavra_forca = ["_" for i in uma_palavra]
chance = 1
while (chance < 7 and palavra_forca.count("_") != 0):
    letra = input("Digite uma letra: ")
    if (letra in uma_palavra):  # verifica se a palavra tem a letra digitada
        print("A palavra é: ", end=" ")
        for p in range(len(uma_palavra)):
            if letra == uma_palavra[p]:
                del palavra_forca[p]
                palavra_forca.insert(p, letra)
        print(" ".join(palavra_forca))
    else:
        print("-> Você errou pela " + str(chance) + "a vez. Tente de novo!")
        chance = chance + 1

if palavra_forca.count("_") == 0:
    print("Parabéns! Você acertou a palavra.")
else:
    print("Forca! Fim de jogo.")
