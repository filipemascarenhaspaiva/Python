'''Crie um código em Python que pede qual tabuada o usuário 
quer ver, em seguida imprima essa tabuada.'''

num1 = int(input('VocÊ quer saber a tabuada de que numero?\n'))

for num2 in range(1, 10+1):
    print(num1, 'x', num2, '=', num1*num2)
