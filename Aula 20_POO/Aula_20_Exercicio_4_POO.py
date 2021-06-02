'''4. Crie uma classe para representar um jogador de futebol, com
os atributos nome, posição, data de nascimento, nacionalidade,
altura e peso. Crie os métodos públicos necessários para sets e
gets e também um método para imprimir todos os dados do jogador.
Crie um método para calcular a idade do jogador e outro método para
mostrar quanto tempo falta para o jogador se aposentar. Para isso,
considere que os jogadores da posição de defesa se aposentam em média
aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35'''


class Jogador():
    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def calculo_idade(self):
        idade = 2021 - self.nascimento
        return idade

    def tempo_atacante(self):
        return 35 - Jogador.calculo_idade(self)

    def tempo_meio(self):
        return 38 - Jogador.calculo_idade(self)

    def tempo_defesa(self):
        return 40 - Jogador.calculo_idade(self)

    def dados(self):
        print(self.nome, self.posicao, self.nascimento,
              self.nacionalidade, self.altura, self.peso)


nome_j = input('Nome do jogador?: ')
posicao_j = input(
    'Qual a posição do jogador atacante,meio de campo ou defesa?: ').lower()
nacionalidade_j = input('Qual a nacionalidade do jogador?: ')
nascimento_j = int(input('Em qual ano o jogador nasceu?: '))
altura_j = float(input('Qual a altura do jogador?: '))
peso_j = float(input('Qual o peso do jogador?: '))

jogador = Jogador(nome_j, peso_j, nascimento_j,
                  nacionalidade_j, altura_j, peso_j)
print()
print('Ele tem ', jogador.calculo_idade(), 'Anos aproximadamente')
print()
if posicao_j == 'defesa':
    print('faltam ', jogador.tempo_defesa(), 'para ele se aposentar')
elif posicao_j == 'atacante':
    print('faltam ', jogador.tempo_atacante(), 'para ele se aposentar')
elif posicao_j == 'meio de campo':
    print('faltam ', jogador.tempo_meio(), 'para ele se aposentar')
print()
print('Os dados do seu jogador são:: ', jogador.dados())
