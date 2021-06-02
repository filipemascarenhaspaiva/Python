'''2. Considere a classe ContaBancaria com os seguintes atributos: 
número,agência, saldo e código_tipo (código 1 = Conta Corrente, 
código 2 = Conta Poupança). Crie uma classe ContaImposto que herda 
de conta e possui um atributo percentualImposto. Esta classe também 
deve possuir um método calcularImposto() que subtrai do saldo,
o valor do próprio saldo multiplicado pelo percentual do imposto. 
Crie um programa para criar as instâncias de ContaImposto e 
utilizar todos os métodos das 3 classes (ex.: sacar, depositar,calcularImposto).'''


class ContaBancaria():
    def __init__(self, numero, agencia, saldo, codigo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.codigo = codigo

    def sacar(self, saque):
        self.saldo = self.saldo - saque
        print('Sacando R$ ', saque, 'seu saldo fica em R$ ', self.saldo)

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        print('Depositando R$ ', deposito,
              'seu saldo fica em R$ ', self.saldo)


class ContaImposto(ContaBancaria):
    def __init__(self, numero, agencia, saldo, codigo):
        super().__init__(numero, agencia, saldo, codigo)
        self.percentualimposto = 30/100

    def calculaImposto(self):
        self.saldo = self.saldo - (self.percentualimposto * self.saldo)
        print('Com o imposto pago seu saldo ficou em R$ ', self.saldo)


print('                 Cadastre seus dados bancarios: ')
print()
numero = int(input('informe o numero da sua conta: '))
agencia = input('infomre sua agencia bancaria: ')
codigo = input('informe se é conta-corrente ou poupança: ')
saldo = float(input('Informe seu saldo: '))
print()

conta = ContaBancaria(numero, agencia, saldo, codigo)
imposto = ContaImposto(numero, agencia, saldo, codigo)
print('1. Sacar')
print('2. Depositar')
print('3. Pagar imposto')
print()
escolha = input('Deseja sacar, depositar ou pagar seu imposto?: ').lower()

if escolha == '1':
    valor_saque = float(input('Qual o valor que deseja sacar?: '))
    conta.sacar(valor_saque)
elif escolha == '2':
    valor_depositar = float(input('Qual o valor que deseja depositar?: '))
    conta.depositar(valor_depositar)
elif escolha == '3':
    imposto.calculaImposto()
else:
    print('Opção invalida')
