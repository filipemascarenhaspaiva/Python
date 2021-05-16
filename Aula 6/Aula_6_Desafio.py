'''DESAFIO -  Data com mês por extenso. Construa
uma função que receba uma data no formato DD/MM/AAAA
e devolva uma string no formato D de mesPorExtenso 
de AAAA. Opcionalmente, valide a data e retorne NULL
caso a data seja inválida. Considere que Fevereiro 
tem 28 dias e que a cada 4 anos temos ano bisexto, 
sendo que nesses casos Fevereiro terá 29 dias.'''

dia = int(input('Informe o dia em formato DD:  '))
mes = int(input('Informe o mes em formato MM:  '))
ano = int(input('Informe o ano em formato AAAA:  '))


def data(dia, mes, ano):
    if 1 <= dia <= 31 and 1 <= mes <= 12 and 0 <= ano <= 2021:
        if mes == 1 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de janeiro de {ano}')
        if mes == 2 and 1 <= dia <= 29 and 0 <= ano <= 2020 and ano % 4 == 0:
            print(f'{dia} de fevereiro de {ano}')
            if mes == 2 and 1 <= dia <= 28 and 0 <= ano <= 2021 and ano % 4 > 0:
                print(f'{dia} de fevereiro de {ano}')
        if mes == 3 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de março de {ano}')
        if mes == 4 and 1 <= dia <= 30 and 0 <= ano <= 2021:
            print(f'{dia} de abril de {ano}')
        if mes == 5 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de maio de {ano}')
        if mes == 6 and 1 <= dia <= 30 and 0 <= ano <= 2021:
            print(f'{dia} de junho de {ano}')
        if mes == 7 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de julho de {ano}')
        if mes == 8 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de agosto de {ano}')
        if mes == 9 and 1 <= dia <= 30 and 0 <= ano <= 2021:
            print(f'{dia} de setembro de {ano}')
        if mes == 10 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de outubro de {ano}')
        if mes == 11 and 1 <= dia <= 30 and 0 <= ano <= 2021:
            print(f'{dia} de novembro de {ano}')
        if mes == 12 and 1 <= dia <= 31 and 0 <= ano <= 2021:
            print(f'{dia} de dezembro de {ano}')
    else:
        print('Null')


data(dia, mes, ano)
