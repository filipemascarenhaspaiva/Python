'''PROJETO: Gastos com viagem -  Escrever uma
aplicação utilizando funções que calcule os gastos
com passagem, hospedagem, aluguel de carro e gastos
extras de uma viagem para uma determinada cidade.

Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba
um parâmetro (argumento) chamado 'noites' e retorne
o custo total do hotel, sendo que 1 noite custa
R$ 140,00.'''

noites = int(input('Quantas noites ficar no hotel: '))


def custo_hotel(noites):
    return noites * 140


print(custo_hotel(noites))

'''Passagem
2 - Crie uma função chamada 'custo_aviao' que receba
o nome da cidade e retorne o custo da passagem de
avião, sendo que passagem para:

- São Paulo custa R$ 312,00;

- Porto Alegre custa R$ 447,00;

- Recife custa R$ 831,00;

- Manaus custa R$ 986,00.'''

nome_cidade = input(
    'Pretende ir para São Paulo, Porto Alegre, Recife ou Manaus: ')
custo_SP = 447.00
custo_PA = 312.00
custo_RE = 831.00
custo_MA = 986.00


def custo_aviao(nome_cidade):
    if nome_cidade == 'São Paulo':
        return custo_SP
        print(f'O valor da passagem será de R$ {custo_SP}')
    if nome_cidade == 'Porto Alegre':
        return custo_PA
        print(f'O valor da passagem será de R$ {custo_PA}')
    if nome_cidade == 'Recife':
        return custo_RE
        print(f'O valor da passagem será de R$ {custo_RE}')
    if nome_cidade == 'Manaus':
        return custo_MA
        print(f'O valor da passagem será de R$ {custo_MA}')


custo_aviao(nome_cidade)

'''Aluguel de Carro
3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.

- Calcule o custo do aluguel do carro sendo que:

- A cada dia o carro custa R$ 40,00;

- Alugando 7 dias ou +: R$ 50,00 de desconto;

- Alugando 3 dias ou +: R$ 20,00 de desconto;

- Você pode receber apenas um desconto;

- Retorne o custo.'''

dias = int(input('vai alugar o carro por quantos dias: '))


def custo_carro(dias):
    if dias < 3:
        print(f'O custo do aluguel do veiculo fica em {40*dias}')
    if 3 <= dias < 7:
        print(f'O custo do aluguel do veiculo fica em {40*dias - 20}')
    if dias >= 7:
        print(f'O custo do aluguel do veiculo fica em {40*dias-50}')


custo_carro(dias)

'''Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.

- Reutilize as funções já criadas.

- Exiba o total da viagem chamando apenas a nova função declarada!'''
x = custo_aviao(nome_cidade)
y = custo_hotel(noites)


def custo_total(x, y):
    print(f'O custo total da viagem será de {x+y}')


custo_total(x, y)

'''Gastos Extras
5 - Modifique essa nova função criada e adicione um 
terceiro argumento: 'gastos_extras' e some esse valor
ao total da viagem.

Exiba no console o custo total de uma viagem de 12 
dias para 'Manaus' gastando R$ 800,00 adicionais.'''

x = custo_aviao(nome_cidade)
y = custo_hotel(noites)
gastos_extras = float(input('Insira os gastos extras: '))


def custo_total(x, y, gastos_extras):
    print(f'O custo total da viagem será na verdade {x+y+gastos_extras}')


custo_total(x, y, gastos_extras)
