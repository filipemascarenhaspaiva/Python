'''Exercicio 2 Escreva uma função que recebe dois 
números (a e b) como parâmetro e retorna True caso 
a soma dos dois seja maior que um terceiro parâmetro,
chamado limite.'''

x = float(input('insira um valor: '))
y = float(input('insira um valor: '))
z = 10


def comparacao(x, y, z):
    if x + y > z:
        print('true')
    else:
        print('False')


comparacao(x, y, z)
