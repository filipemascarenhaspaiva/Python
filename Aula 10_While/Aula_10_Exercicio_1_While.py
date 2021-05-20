'''Exercício 1 - Escreva um programa que pede a senha ao usuário, e 
só sai do looping quando digitarem corretamente a senha.'''

senha = 'blue'
tentativa = input('Digite a senha: ')
while tentativa != senha:
    print('Senha incorreta')
    tentativa = input('Digite a senha: ')

if tentativa == senha:
    print('A Senha esta correta. Acesso liberado')
