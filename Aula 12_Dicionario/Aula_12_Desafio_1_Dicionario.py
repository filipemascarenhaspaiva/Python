'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela. A média para
aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de
recuperação, caso contrário é reprovado.'''

aluno = {}

aluno['nome'] = input('digite o nome do aluno: ')
aluno['nota'] = int(input('Digite a nota do aluno: '))

if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['nota'] >= 5 and aluno['nota'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(aluno.values())
