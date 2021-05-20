'''Exericio 1- Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
aos quadrados desses números.'''
numeros = [1, 4, 5, 6, 7, 8]
quadrados = {}
for i in numeros:
    quadrados[i] = i**2
print(quadrados)
