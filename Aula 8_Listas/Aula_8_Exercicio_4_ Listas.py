'''Dada uma string com uma frase informada pelo 
usuário (incluindo espaços em branco), conte quantas 
vezes aparece uma vogal.'''


def conta_vogal(palavra):
    vogais = 0

    for letra in palavra:
        if letra.upper() in "AEIOU":
            vogais += 1
    return vogais


frase = input("Digite uma palavra ou frase para contarmos as vogais: ")
print("A palavra/frase", frase, "possui", conta_vogal(frase), "vogais")
