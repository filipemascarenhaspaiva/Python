'''Exercício 2 - Faça um programa que leia dez conjuntos de dois 
valores, o primeiro representando o número do aluno e o segundo 
representando a sua altura em centímetros.  Encontre o aluno mais 
alto e o mais baixo. Mostre o número do aluno mais alto e o número 
do aluno mais baixo, junto com suas alturas.'''

turma = []

num_alunos = int(input('Quantos alunos: '))

for alturas in range(num_alunos):

    alturas = int(input('Digite as alturas: '))

    turma.append(alturas)

print("O aluno com maior altura tem ", max(turma),
      "\nO aluno com menor altura tem :", min(turma)),
