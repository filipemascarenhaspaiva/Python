'''Desenvolva um código que pergunte um número n para o usuário e 
exiba todos seus divisores. Caso seja um número primo, o programa 
ainda deve informar que se trata de um número primo! '''

n = int(input("Digite um número inteiro: "))

divisores = []
for i in range(n, 0, -1):
    if(n % i == 0):
        divisores.append(i)
print("Os divisores de", n, "são:")

for item in divisores:
    print(item)

if len(divisores) == 2:
    print(n, "é um número primo!")
