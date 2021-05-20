'''Exercício 1 Escreva uma função que recebe dois 
parâmetros (números) e imprime o menor dos dois. 
Se eles forem iguais, imprima que são valores idênticos.'''

x = float(input('Informe um valor: '))
y = float(input('Informe um valor: '))


def valores(x, y):
    if x < y:
        print(f'{x} é menor que {y}')
    if y < x:
        print(f'{y} é menor que {x}')
    if x == y:
        print('São iguais')


valores(x, y)
