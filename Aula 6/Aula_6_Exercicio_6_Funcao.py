'''Escreva uma função que, dado um número nota 
representando a nota de um estudante, converte o 
valor de nota para um conceito (A, B, C, D, E e F).


Nota	Conceito
>=9.0	A
>=8.0	B
>=7.0	C
>=6.0	D
>4.0    E
<=4.0	F'''

nota = float(input('Informe a nota do aluno: '))


def conceito_nota(nota):
    if 9 <= nota <= 10:
        print('A')
    elif 8 <= nota <= 9:
        print('B')
    elif 7 <= nota <= 8:
        print('C')
    elif 6 <= nota <= 7:
        print('D')
    elif 4 < nota < 6:
        print('E')
    elif 0 <= nota <= 4:
        print('F')
    else:
        print('Nota invalida')


conceito_nota(nota)
