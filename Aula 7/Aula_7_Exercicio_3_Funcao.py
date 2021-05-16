'''Exercicio 3 Crie uma função que receba uma string 
como argumento e retorne a mesma string em letras 
maiúsculas. Faça uma chamada à função, passando 
como parâmetro uma string.'''

palavra = input('Escreva uma palavra em minusculo: ')


def minuscula(palavra):
    print(f'{palavra.upper()}')


minuscula(palavra)
