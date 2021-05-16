'''Utilizando listas faça um programa que faça 5 
perguntas para uma pessoa sobre um crime. As 
perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"  

O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. Se a pessoa 
responder positivamente a 2 questões ela deve ser 
classificada como "Suspeita", entre 3 e 4 como 
"Cúmplice" e 5 como "Assassino". Caso contrário, 
ele será classificado como "Inocente".'''

lista = ['Telefonou para a vítima?', 'Esteve no local do crime',
         'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

contador = 0
for pergunta in lista:
    a = input(pergunta).lower()
    if a == 'sim':
        contador += 1

if 0 <= contador < 2:
    print('Inocente')
elif contador == 2:
    print('Suspeita')
elif 3 <= contador <= 4:
    print('Cumplice')
elif contador == 5:
    print('Assassino')
