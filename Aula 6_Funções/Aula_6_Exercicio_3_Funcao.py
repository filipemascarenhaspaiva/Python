'''Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um
item antes do imposto. A função “altera” o valor de 
custo para incluir o imposto sobre vendas.'''

custo = float(input('Digite o valor inicial do produto antes do reajsute: '))
taxaImposto = float(input('Digite a taxa do imposto: '))
custo_alterado = custo * taxaImposto/100 + custo


def somaImposto(taxaImposto, custo):
    return print(f'O item custava R$ {custo} e com o incremento do imposto de {taxaImposto}% o valor final do item é de R$ {custo_alterado}')


somaImposto(taxaImposto, custo)
