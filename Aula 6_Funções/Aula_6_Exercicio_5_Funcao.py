'''Faça um programa que calcule através de uma função
o IMC de uma pessoa que tenha 1,68 e pese 75kg.'''

peso = float(input('Informe o valor do seu peso: '))
altura = float(input('Informe o valor da sua altura: '))
calculo = peso / altura * altura


def imc(calculo):
    return print(f'Seu IMC é {calculo}')


imc(calculo)
