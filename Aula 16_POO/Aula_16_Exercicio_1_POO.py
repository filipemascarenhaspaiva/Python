'''Exercicio 1'''


class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dados(self):
        print(
            f' nome: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}')


cadastro = pessoa('Filipe', 'Paiva', 20)
cadastro.dados()
