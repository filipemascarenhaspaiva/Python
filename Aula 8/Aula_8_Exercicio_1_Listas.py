'''Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva 
um programa que imprima as seguintes informações:

tamanho da lista.
maior valor da lista.
menor valor da lista.
soma de todos os elementos da lista.
lista em ordem crescente.
lista em ordem decrescente.'''

lista = [5, 7, 2, 9, 4, 1, 3]

print(f'O tamanho da lista é de {len(lista)} elementos')
print(f'O maior elemento da lista é o {max(lista)}')
print(f'O menor elemento da lista é o {min(lista)}')
print(f'A soma de todos os elementos da lista é de {sum(lista)}')

lista.sort()

print(f'Em ordem crescente a lista se caracteriza desta forma {lista}')

lista.reverse()

print(f'Em ordem decrescente a lista se caracteriza desta forma {lista}')
