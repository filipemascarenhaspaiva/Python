'''Exercicio 5 - O Sr. Manoel Joaquim expandiu seus negócios para 
além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores 
referentes aos preços das mercadorias. Um valor zero deve ser 
informado pelo operador para indicar o final da compra. O programa 
deve então mostrar o total da compra e perguntar o valor em 
dinheiro que o cliente forneceu, para então calcular e mostrar o 
valor do troco. Após esta operação, o programa deverá voltar ao 
ponto inicial, para registrar a próxima compra. A saída deve ser 
conforme o exemplo abaixo:

Lojas Tabajara
Produto 1: R$ 2.00
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00 
Troco: R$ 11.00'''

print('Lojas Tabajara')
num_produto = 1
valores = []
while True:
    valor_produto = float(input(f'Produto {num_produto}: R$ '))
    valores.append(valor_produto)
    num_produto += 1
    if valor_produto == 0:
        break
    continue
print('Total: R$ ', sum(valores))
Dinheiro = float(input('Dinheiro: R$ '))
Troco = Dinheiro - sum(valores)
print(f'Troco: R$ {Troco}')
