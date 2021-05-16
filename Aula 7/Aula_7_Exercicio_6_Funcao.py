'''Exercicio 6 Um professor, muito legal, fez 3 
provas durante um semestre, mas só vai levar em 
conta as duas notas mais altas para calcular a média.

Faça uma aplicação que peça o valor das 3 notas, 
mostre como seria a média com essas 3 provas(notas?), a 
média com as 2 notas mais altas, bem como sua nota 
mais alta e sua nota mais baixa.'''

nota_1 = float(input('Digite sua nota de 0 à 10: '))
nota_2 = float(input('Digite sua nota de 0 à 10: '))
nota_3 = float(input('Digite sua nota de 0 à 10: '))
media = (nota_1+nota_2+nota_3) / 3


def media_real(media):
    print(f'sua media usando as três notas é {media}: ')


def media_alta_M1_2(nota_1, nota_2):
    print(f'sua média é {(nota_1+nota_2)/2}')


def media_alta_M1_3(nota_1, nota_3):
    print(f'sua média é {(nota_1+nota_3)/2}')


def media_alta_M2_1(nota_2, nota_1):
    print(f'sua média é {(nota_2+nota_1)/2}')


def media_alta_M2_3(nota_2, nota_3):
    print(f'sua média é {(nota_2+nota_3)/2}')


def media_alta_M3_1(nota_3, nota_1):
    print(f'sua média é {(nota_3+nota_1)/2}')


def media_alta_M3_2(nota_3, nota_2):
    print(f'sua média é {(nota_3+nota_2)/2}')


def picos_M1_m2(nota_1, nota_2):
    print(f'sua maior nota é {nota_1} e sua menor nota é {nota_2}')


def picos_M1_m3(nota_1, nota_3):
    print(f'sua maior nota é {nota_1} e sua menor nota é {nota_3}')


def picos_M2_m1(nota_2, nota_1):
    print(f'sua maior nota é {nota_2} e sua menor nota é {nota_1}')


def picos_M2_m3(nota_2, nota_3):
    print(f'sua maior nota é {nota_2} e sua menor nota é {nota_3}')


def picos_M3_m1(nota_3, nota_1):
    print(f'sua maior nota é {nota_3} e sua menor nota é {nota_1}')


def picos_M3_m2(nota_3, nota_2):
    print(f'sua maior nota é {nota_3} e sua menor nota é {nota_2}')


media_real(media)
if nota_1 > nota_2 and nota_3:
    if nota_2 > nota_3:
        media_alta_M1_2(nota_1, nota_2)
    elif nota_3 > nota_2:
        media_alta_M1_3(nota_1, nota_3)
if nota_2 > nota_3 and nota_1:
    if nota_1 > nota_3:
        media_alta_M2_1(nota_2, nota_1)
    elif nota_3 > nota_1:
        media_alta_M2_3(nota_2, nota_3)
if nota_3 > nota_1 and nota_2:
    if nota_1 > nota_2:
        media_alta_M3_1(nota_3, nota_1)
    if nota_2 > nota_1:
        media_alta_M3_2(nota_3, nota_2)


if nota_1 > nota_2 and nota_3:
    if nota_2 < nota_3:
        picos_M1_m2(nota_1, nota_2)
    elif nota_3 < nota_2:
        picos_M1_m3(nota_1, nota_3)
if nota_2 > nota_1 and nota_3:
    if nota_1 < nota_3:
        picos_M2_m1(nota_1, nota_2)
    elif nota_3 < nota_1:
        picos_M2_m3(nota_1, nota_3)
if nota_3 > nota_1 and nota_2:
    if nota_1 < nota_2:
        picos_M3_m1(nota_1, nota_2)
    elif nota_2 < nota_1:
        picos_M3_m2(nota_1, nota_3)
