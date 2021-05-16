'''Faça um programa que calcule o salário de
um colaborador na empresa XYZ. O salário é pago
conforme a quantidade de horas trabalhadas. Quando
um funcionário trabalha mais de 40 horas ele recebe
um adicional de 1.5 nas horas extras trabalhadas.'''

salario_inicial = float(input('Valor base do salario do colaborador: '))
horas_trabalhadas = float(
    input('Digite quantas horas trabalhadas o colaborador tem: '))
adicional = 1.5
salario_final = (horas_trabalhadas - 40) * adicional + salario_inicial


def salario(salario_final):
    return print(f'O funcionario vai receber R$ {salario_final} de salario')


salario(salario_final)
