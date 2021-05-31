class Conta():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self):
        while True:
            saque1 = input('deseja sacar(S ou N): ').upper()
            if saque1 == 'S':
                saque2 = int(input('Qual o valor que deseja sacar?: '))
                if saque2 > self.saldo:
                    print('Valor de saque invalido')
                elif saque2 < self.saldo or saque2 == self.saldo:
                    print('Seu novo saldo é de ', self.saldo - saque2)
                    break
            elif saque1 == 'N':
                break
            else:
                continue
        while True:
            self.saldo = self.saldo - saque2
            depositar1 = input('Deseja depositar um valor(S ou N): ').upper()
            if depositar1 == 'S':
                depositar2 = int(input('Qual o valor que deseja depositar?: '))
                if depositar2 <= 0:
                    print('Valor de deposito invalido')
                else:
                    print('Seu novo saldo é de ', depositar2 + self.saldo)
                    break
            elif depositar1 == 'N':
                break
            else:
                continue


nome = input('Qual o nome do titular?: ')
valor = int(input('Qual o valor do saldo?: '))

cadastro = Conta(nome, valor)
cadastro.sacar()
