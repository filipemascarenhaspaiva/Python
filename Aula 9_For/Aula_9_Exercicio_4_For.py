'''Crie um código em Python que receba uma lista de nomes informados
 pelo usuário com tamanho indefinido (a lista deve ser encerrada 
 quando o usuário digitar 0) e, na sequência, receba um nome para 
 que seja verificado se este consta na lista ou não. Observação: 
 ignorar diferenças entre maiúsculas e minúsculas.'''

nomes = []

for i in range(1000):
    a = input("Digite um nome para acrescentar à lista ou 0 para sair: ").lower()
    if a == '0':
        break
    else:
        nomes.append(a)

nome = input("Digite um nome a ser buscado na lista: ").lower()
if nome in nomes:
    print("O nome está na lista!")
else:
    print("O nome NÃO está na lista!")
