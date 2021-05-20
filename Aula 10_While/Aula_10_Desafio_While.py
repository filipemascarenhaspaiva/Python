'''DESAFIO - Desenvolver um programa para verificar a nota do aluno
em uma prova com 10 questões, o programa deve perguntar ao aluno a
resposta de cada questão e ao final comparar com o gabarito da
prova assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se
outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:

-Maior e Menor Acerto;

-Total de Alunos que utilizaram o sistema;

-A Média das Notas da Turma.

# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

-Após concluir isto você poderia incrementar o programa permitindo
que o professor digite o gabarito da prova # antes dos alunos
usarem o programa.'''

notas_alunos = []
print('Digite a alternatica correta de cada questão abaixo(maiusculo): ')

questao_1 = input('Questão 1: ')
questao_2 = input('Questão 2: ')
questao_3 = input('Questão 3: ')
questao_4 = input('Questão 4: ')
questao_5 = input('Questão 5: ')
questao_6 = input('Questão 6: ')
questao_7 = input('Questão 7: ')
questao_8 = input('Questão 8: ')
questao_9 = input('Questão 9: ')
questao_10 = input('Questão 10: ')

print('Digite a alternativa marcada em cada questão: ')

while True:
    contador_acertos = 0
    Resposta_1 = input('Questão 1- ').upper()
    Resposta_2 = input('Questão 2- ').upper()
    Resposta_3 = input('Questão 3- ').upper()
    Resposta_4 = input('Questão 4- ').upper()
    Resposta_5 = input('Questão 5- ').upper()
    Resposta_6 = input('Questão 6- ').upper()
    Resposta_7 = input('Questão 7- ').upper()
    Resposta_8 = input('Questão 8- ').upper()
    Resposta_9 = input('Questão 9- ').upper()
    Resposta_10 = input('Questão 10- ').upper()
    if Resposta_1 == questao_1:
        contador_acertos += 1
    if Resposta_2 == questao_2:
        contador_acertos += 1
    if Resposta_3 == questao_3:
        contador_acertos += 1
    if Resposta_4 == questao_4:
        contador_acertos += 1
    if Resposta_5 == questao_5:
        contador_acertos += 1
    if Resposta_6 == questao_6:
        contador_acertos += 1
    if Resposta_7 == questao_7:
        contador_acertos += 1
    if Resposta_8 == questao_8:
        contador_acertos += 1
    if Resposta_9 == questao_9:
        contador_acertos += 1
    if Resposta_10 == questao_10:
        contador_acertos += 1
    notas_alunos.append(contador_acertos)
    adicionar_aluno = input(
        'outro aluno vai utilizar o sistema, sim ou não: ').lower()
    if adicionar_aluno == 'sim':
        contador_acertos == 0
        continue
    if adicionar_aluno == 'não':
        break

print('A maior nota da turma foi', max(notas_alunos))
print('A menor nota da turma foi', min(notas_alunos))
print('foram', len(notas_alunos), 'alunos que fizeram a prova')
print('A media da nota da turma foi', sum(notas_alunos) // len(notas_alunos))
