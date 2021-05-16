'''Escreva um programa onde o usuário digita uma frase e essa frase 
retorna sem nenhuma vogal.'''


def some_vogal(frase):
    vogais = "aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî"
    for letra in vogais:
        if letra in frase:
            frase = frase.replace(letra, "")
    return frase


str_frase = input("Digite uma palavra ou frase para retirarmos as vogais: ")
print("A palavra ou frase '", str_frase, "' fica '",
      some_vogal(str_frase), "' sem as vogais")
