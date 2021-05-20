'''1. Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
retornar a data completa. Não esqueça de validar se a celebridade escolhida está
presente em seu dicionário.'''

print('Seja bem-vindo ao nosso calendário. Sabemos a data de nascimento das seguintes celebridades:')
print()
print('Rafael Lange')
print('Cauê Moura')
print('Neil deGrasse Tyson')
print('Taylor Davis')
print('Garry Kasparov')
print('Gugu Mbatha-Raw')
print()

famosos = {'Rafael Lange': '11/02/97', 'Cauê Moura': '11/11/87', 'Neil deGrasse Tyson': '05/10/58',
           'Taylor Davis': '20/03/87', 'Garry Kasparov': '13/04/63', 'Gugu Mbatha-Raw': '21/04/83'}
while True:
    famoso = input('De quem você gostaria de saber a data de nascimento?: ')
    if famoso == 'Rafael Lange':
        print('Ele nasceu em ', famosos['Rafael Lange'])
        continue
    if famoso == 'Cauê Moura':
        print('Ele nasceu em ', famosos['Cauê Moura'])
        continue
    if famoso == 'Neil deGrasse Tyson':
        print('Ele nasceu em ', famosos['Neil deGrasse Tyson'])
        continue
    if famoso == 'Taylor Davis':
        print('Ela nasceu em ', famosos['Taylor Davis'])
        continue
    if famoso == 'Garry Kasparov':
        print('Ele nasceu em ', famosos['Garry Kasparov'])
        continue
    if famoso == 'Gugu Mbatha-Ra':
        print('Ela nasceu em ', famosos['Gugu Mbatha-Ra'])
        continue
    if famoso != 'Gugu Mbatha-Ra' and famoso != 'Gary Kasparov' and famoso != 'Taylor Davis' and famoso != 'Neil deGrasse Tyson' and famoso != 'Cauê Moura' and famoso != 'Rafael Lange':
        print('Desculpe, ainda não temos a data de nascimento deste famoso')
        break
