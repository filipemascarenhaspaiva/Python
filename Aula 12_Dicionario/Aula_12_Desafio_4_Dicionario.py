'''DESAFIO: Crie um programa que leia nome, sexo e idade de várias 'pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.'''

print('Cadastre até 5 pessoas')
print()

contador = 0
cadastrado_1 = {}
cadastrado_2 = {}
cadastrado_3 = {}
cadastrado_4 = {}
cadastrado_5 = {}

mulheres = []
idades = []
while contador != 5:
    nome = input('Insira seu nome: ')
    idade = int(input('Insira sua idade: '))
    if idade != 0:
        idades.append(idade)
    while True:
        sexo = input(
            'Digite M se for do sexo masculino,F se for feminino,NB se for não-binário: ').upper()
        if sexo == 'M' or sexo == 'F' or sexo == 'NB':
            break
        else:
            print('Sexo invalido')
            continue
    contador += 1
    if contador == 1:
        cadastrado_1['Nome'] = nome
        cadastrado_1['Idade'] = idade
        cadastrado_1['Sexo'] = sexo
    if contador == 2:
        cadastrado_2['Nome'] = nome
        cadastrado_2['Idade'] = idade
        cadastrado_2['Sexo'] = sexo
    if contador == 3:
        cadastrado_3['Nome'] = nome
        cadastrado_3['Idade'] = idade
        cadastrado_3['Sexo'] = sexo
    if contador == 4:
        cadastrado_4['Nome'] = nome
        cadastrado_4['Idade'] = idade
        cadastrado_4['Sexo'] = sexo
    if contador == 5:
        cadastrado_5['Nome'] = nome
        cadastrado_5['Idade'] = idade
        cadastrado_5['Sexo'] = sexo
    if sexo == 'F':
        mulheres.append(nome)
    while True:
        decidir = input('Colocar mais uma pessoa(sim ou não): ').lower()
        if decidir == 'sim':
            break
        if decidir == 'não':
            break
        else:
            print('palavra-Chave invalida')
        continue
    if decidir == 'não':
        break
    if decidir == 'sim':
        continue
cadastrados = [cadastrado_1, cadastrado_2,
               cadastrado_3, cadastrado_4, cadastrado_5]
media_idades = sum(idades) // contador
print(f'Temos {contador} pessoas cadastradas')
print(f'a média da idade de nossos filiados é de {media_idades} anos')
print(mulheres)
