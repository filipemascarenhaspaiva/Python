'''Exercicio 2- Crie um dicionário em que suas chaves correspondem a números
inteiros entre [1, 10] e cada valor associado é o número ao quadrado.'''

quadrados = {}
for i in range(1, 11):
    quadrados[i] = i**2
print(quadrados)
