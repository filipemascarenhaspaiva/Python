'''Escreva uma função que recebe dois parâmetros e
imprime o menor dos dois. Se eles forem iguais,
imprima que eles são iguais'''

x = float(input('Digite um valor: '))
y = float(input('Digite um valor '))


def comparacao(x, y):
    if x > y:
        print(f'{x} é maior que {y}')
    elif y > x:
        print(f'{y} é maior que {x}')
    else:
        print('eles são iguais')


comparacao(x, y)
