vingadores = {'Chris Evans': 'Capitão América', 'Mark Rufallo': 'Hulk', 'Tom Hiddleston': 'Loki',
              'Chris Hemworth': 'Thor', 'Robert Downey Jr': 'Homem de ferro', 'Scarlett Johansson': 'Viuva Negra'}
'''
vingadores['Mick Castle'] = "Michael Myers"
vingadores['Gal Gadot'] = "Mulher Maravilha"
vingadores['Joaquim Phoenix'] = "Coringa"

print(vingadores)
del vingadores['Mark Rufallo']
print(vingadores.pop('Chris Hemworth', 'Blaaa'))'''

Liga = {'Henry Cavill': 'Superman', 'Gal Gadot': 'Mulher Maravilha',
        'Ezra Miller': 'Flash', 'Jason Momoa': 'Aquaman', 'Ray Ficher': 'Cyborgue'}

for personagem in Liga:
    vingadores[personagem] = Liga[personagem]
print(vingadores)
