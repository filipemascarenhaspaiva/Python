'''4. Uma escola te contratou para desenvolver um programa em Python para que o
professor gerencie as notas de seus alunos. Seu programa deve apresentar o seguinte
menu:

0. Sair
1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
2. Inserir aluno e nota
3. Alterar a nota de um aluno
4. Consultar nota de um aluno específico
5. Apagar um aluno da lista
6. Exibir a média da turma

As notas e os nomes dos alunos serão fornecidos pelo professor. Implemente a sua
solução utilizando dicionário.'''

turma = {}

while True:

    print('0. Sair')
    print()
    print('1. Exibir lista de alunos com suas notas(cada aluno tem uma nota)')
    print()
    print('2. inserir aluno e nota')
    print()
    print('3. Alterar a nota de um aluno')
    print()
    print('4. Consultar nota de um aluno específico')
    print()
    print('5. Apagar um aluno da lista')
    print()
    print('6. Exibir a média da turma')
    print()

    comando = input('')

    if comando == '2':
        while comando == '2':
            aluno = input('Insira o nome do aluno: ')
            nota = float(input('Insira a nota deste aluno: '))
            turma[aluno] = nota
            comando = input(
                'Digite 2 para inserir mais um aluno ou 0 para prossegui: ')

    if comando == '1':
        print(turma)
    if comando == '3':
        nome_aluno = input(
            'Digite o nome do aluno que deseja alterar a nota: ')
        nova_nota = float(input('Digite a nova nota do aluno: '))
        turma[nome_aluno] = nova_nota
        continue
    if comando == '4':
        nome_aluno = input(
            'Digite o nome do aluno que deseja verificar a nota: ')
        print(nome_aluno, 'Tirou ', turma[nome_aluno])
    if comando == '5':
        nome_aluno = input(
            'Digite o nome do aluno que deseja apagar dos registros: ')
        turma.pop(nome_aluno, 'Este aluno não consta nos nossos registros')
    if comando == '6':
        print('A média de todas as notas cadastradas é ',
              sum(turma.values())//len(turma))
