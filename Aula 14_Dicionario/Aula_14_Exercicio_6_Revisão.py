
lista = [1, 2, 3, 4, 5]
contador = 0
for pergunta in lista:
    if pergunta == lista[0]:
        questão_1 = input(
            'Telefonou para a vítima?(para afirmar digite "sim"): ')
    if pergunta == lista[1]:
        questão_2 = input(
            'Esteve no local do crime?(para afirmar digite "sim"): ')
    if pergunta == lista[2]:
        questão_3 = input('Mora perto da vítima?(para afirmar digite "sim"): ')
    if pergunta == lista[3]:
        questão_4 = input('Devia para a vítima?(para afirmar digite "sim"): ')
    if pergunta == lista[4]:
        questão_5 = input(
            'Já trabalhou com a vítima?(para afirmar digite "sim"): ')

if questão_1 == 'sim':
    contador += 1
if questão_2 == 'sim':
    contador += 1
if questão_3 == 'sim':
    contador += 1
if questão_4 == 'sim':
    contador += 1
if questão_5 == 'sim':
    contador += 1

if contador == 0:
    print('Inocente')
if 1 <= contador <= 2:
    print('Suspeito')
if 3 <= contador <= 4:
    print('Cumplice')
if contador == 5:
    print('Assassino')
