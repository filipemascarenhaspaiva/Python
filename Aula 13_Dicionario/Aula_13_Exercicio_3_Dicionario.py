'''3. Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas
de um supermercado. Não esqueça de fazer as seguintes validações:

estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20],
"feijão": [100, 1.50]}

Produto Indisponível

Produto Inválido

Quantidade solicitada não disponível

O programa deverá mostrar para o cliente a quantidade de itens comprados e o total a
pagar.'''

print('Estoque')
print('Temos 1000 tomates custando 2.30 a unidade\n500 alfaces por 0.45\n2001 batatas valendo 1.20 \nNenhuma unidades de feijão')
estoque = {"tomate": [1000, 2.30], "alface": [
    500, 0.45], "batata": [2001, 1.20]}
total_a_pagar = []
contador = 1
while True:
    produto = input('O que vai comprar?: ')
    if produto == 'feijão':
        print('Produto Indisponível')
        continue
    qta = int(input('Quantos(as)?: '))
    if produto == 'tomate':
        if qta <= 1000:
            total_pagar_tomates = qta * 2.30
            total_a_pagar.append(total_pagar_tomates)
        if qta > 1000:
            print('Quantidade Solicitada não disponível')
    if produto == 'alface':
        if qta <= 500:
            total_pagar_alface = qta * 0.45
            total_a_pagar.append(total_pagar_alface)
        if qta > 500:
            print('Quantidade Solicitada não disponível')
    if produto == 'batata':
        if qta <= 2001:
            total_pagar_batata = qta * 1.20
            total_a_pagar.append(total_pagar_batata)
        if qta > 2001:
            print('Quantidade Solicitada não disponível')
    encerrar = input('Deseja encerrar sua compra agora?(sim ou não): ').lower()
    if encerrar == 'sim':
        break
    if encerrar == 'não':
        contador += 1
        continue
print('você comprou', contador, 'items custando um total de ', sum(total_a_pagar))
