'''1. Crie uma classe chamada Ingresso, que possui um valor em 
reais e um método imprimirValor(). Crie uma classe IngressoVIP, 
que herda de Ingresso e possui um valor adicional. Crie um método 
que retorne o valor do ingresso VIP(com o adicional incluído). Crie um programa para criar as 
instâncias de
Ingresso e IngressoVIP, mostrando a diferença de preços.'''


class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimivalor(self):
        print(self.valor)


class IngressoVip(Ingresso):
    def __init__(self, valor, valor_adicional):
        self.valor_adicional = valor_adicional
        super().__init__(valor)

    def valorin_vip(self):
        print(self.valor + self.valor_adicional)


ingresso = Ingresso(15)
ingresso_vip = IngressoVip(15, 5)

ingresso.imprimivalor()

ingresso_vip.valorin_vip()
