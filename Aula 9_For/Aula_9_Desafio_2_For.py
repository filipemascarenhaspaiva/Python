'''Escreva um programa que determine todos os números de 4 algarismos
 que possam ser separados em dois números de dois algarismos que 
 somados e elevando-se a soma ao quadrado obtenha-se o próprio número.

Exemplo: 3025 = 55 e 55**2 é igual á 3025'''

numeros_bizzarros = []
for numero in range(1000, 10000):
    if (numero // 100 + numero % 100)*(numero // 100 + numero % 100) == numero:
        numeros_bizzarros.append(numero)

for num in numeros_bizzarros:
    print(num)
