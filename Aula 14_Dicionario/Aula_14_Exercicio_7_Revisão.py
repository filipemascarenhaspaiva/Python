num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite um valor inteiro: '))
num3 = int(input('Digite um valor inteiro: '))
num4 = int(input('Digite um valor inteiro: '))
num5 = int(input('Digite um valor inteiro: '))
num6 = int(input('Digite um valor inteiro: '))
num7 = int(input('Digite um valor inteiro: '))

numeros_desordenados = []

numeros_desordenados.append(num1)
numeros_desordenados.append(num2)
numeros_desordenados.append(num3)
numeros_desordenados.append(num4)
numeros_desordenados.append(num5)
numeros_desordenados.append(num6)
numeros_desordenados.append(num7)

numeros_desordenados.sort()
numeros_ordenados = []

pares = 'numeros pares: '
impares = 'numeros impares: '

numeros_ordenados.append(pares)
for i in numeros_desordenados:
    if i % 2 == 0:
        numeros_ordenados.append(i)
numeros_ordenados.append(impares)
for i in numeros_desordenados:
    if i % 2 != 0:
        numeros_ordenados.append(i)

print(numeros_ordenados)
print(numeros_desordenados)
