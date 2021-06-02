'''3. Crie uma classe que modele uma pessoa:

a. Atributos: nome, idade, peso e altura.
b. Métodos: envelhecer, engordar, emagrecer, crescer.
Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela 
menor que 21 anos,

ela deve crescer 0,5 cm.'''


class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 5
        print('sua idade agora é ', self.idade)

    def engordar(self, valor_engorda):
        self.peso += valor_engorda
        print('seu peso agora é ', self.peso)

    def emagrecer(self, valor_emagrece):
        self.peso -= valor_emagrece
        print('seu peso agora é ', self.peso)

    def crescer(self):
        self.altura += 0.05
        print('sua altura agora é ', self.altura)


print('Faça seu cadastro para alterar seus atributos: ')
print()
nome = input('Qual o seu nome?: ')
peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual sua altura?: '))
idade = int(input('Qual sua idade?: '))

pessoa = Pessoa(nome, idade, peso, altura)

print("Vamos mudar as coisas agora: ")
print()
altera = input(("Deseja mudar sua idade,peso ou altura?: ")).lower()
print()

if altera == 'idade':
    pessoa.envelhecer()
elif altera == 'peso':
    altera_peso = input('Deseja engordar ou emagrecer?: ').lower()
    if altera_peso == 'engordar':
        quanto_engordar = float(input('Quanto deseja engordar?: '))
        pessoa.engordar(quanto_engordar)
    if altera_peso == 'emagrecer':
        quanto_emagrecer = float(input('Quanto deseja emagrecer?: '))
        pessoa.emagrecer(quanto_emagrecer)

elif altera == 'altura':
    pessoa.crescer()
