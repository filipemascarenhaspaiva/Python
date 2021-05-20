'''Exercicio 4 Crie um programa que tenha uma função 
chamada voto () que vai receber como parâmetro o ano 
de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL ou OBRIGATORIO nas eleições. Para resolver 
esse exercício, pesquise sobre a função date da 
biblioteca Datetime.'''

data_nascimento = int(input('informe sua data de nascimento: '))


def voto(data_nascimento):
    if 0 < data_nascimento <= 2021:
        if 2003 < data_nascimento <= 2005:
            print('voto OPCIONAL')
        if 2005 < data_nascimento <= 2021:
            print('voto NEGADO')
        if data_nascimento <= 2003:
            print('voto OBRIGATORIO')

    else:
        print('Ano invalido')


voto(data_nascimento)
