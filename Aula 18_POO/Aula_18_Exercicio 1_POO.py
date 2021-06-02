while True:
    Escolha = input(
        'Vai colcoar combustivel em dinheiro ou quantidade?(Digite D ou Q): ')
    if Escolha == 'D':
        pagamento = float(input('Vai colocar quanto de combustível?:R$ '))
        break
    elif Escolha == 'Q':
        quantia = float(input('Vai colocar quanto de combustível?:L '))
        break
    else:
        continue
while True:
    alteracoes = input(
        'Deseja alterar o preço,tipo ou quantidade de combustível(tecle P,T ou Q)?: ')
    if alteracoes == 'P':
        novo_preco = float(input('insira o novo preço da gasolina: '))
        break
    elif alteracoes == 'T':
        novo_tipo = input('Insira o tipo de combustível: ')
        break
    elif alteracoes == 'Q':
        nova_quantidade = float(input('Qunato de combustível tem?: '))
        break
    else:
        continue


class bombaCombustível:
    def __init__(self):
        self.tipoCombustível = 'Etanol'
        self.valorLitro = 3
        self.quantidadeCombustivel = 0

    def abastecerPorValor(self):
        return 'Foi colcocado R$ ', pagamento, ' de combustível', 'O veiculo tem agora ', pagamento * self.valorLitro, ' L de combustível'

    def abastecerPorLitro(self):
        return 'Foram colocados L ', quantia, 'de combustível', 'O veiculo tem agora ', self.quantidadeCombustivel + quantia, 'L de combustível'

    def alterarValor(self):
        return self.valorLitro == novo_preco

    def alterarCombustivel(self):
        return self.tipoCombustível == novo_tipo

    def alterarQuantidadeCombustivel(self):
        return self.quantidadeCombustivel == nova_quantidade


bomba = bombaCombustível()
if Escolha == 'D':
    print(bomba.abastecerPorValor())
if Escolha == 'Q':
    print(bomba.abastecerPorLitro())
if alteracoes == 'P':
    print(bomba.alterarValor())
if alteracoes == 'T':
    print(bomba.alterarCombustivel())
if alteracoes == 'Q':
    print(bomba.alterarQuantidadeCombustivel())
