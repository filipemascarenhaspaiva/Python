'''Exercício 0 – Crie um laço while que vai pedir para o usuário 
dois números e faça a soma dos dois. Enquanto a soma não for 50, 
ele deve continuar repetindo.'''

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))

while num1 + num2 != 50:
    print('A soma deles não é 50')
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite um numero: '))
if num1 + num2 == 50:
    print('A soma dos numeros é 50')
