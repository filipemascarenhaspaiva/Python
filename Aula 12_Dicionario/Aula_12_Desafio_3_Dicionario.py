'''Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a
CTPS for diferente de 0, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente , além da idade , com
quantos anos a pessoa vai se aposentar. Considere que o trabalhador
deve contribuir por 35 anos para se aposentar'''

nome = input('Nome Completo: ')
ano_nascimento = int(input('Ano de nascimento: '))
ctps = int(input('Numero da Catteira de Trabalho(Se não houver digite 0): '))
if ctps == 0:
    cadastro = {'Nome': nome, 'Ano de Nascimento': ano_nascimento,
                'Idade': 2021-ano_nascimento, 'Num Carteira de Trabalho': ctps}
else:
    ano_de_contratacao = int(input('Ano de Contratação: '))
    salario = float(input('Salario: '))
    cadastro = {'Nome': nome, 'Ano de Nascimento': ano_nascimento, 'Idade': 2021-ano_nascimento,
                'Aposentadoria': ano_de_contratacao-ano_nascimento+35, 'Num Carteira de Trabalho': ctps, 'Ano de Contratação': ano_de_contratacao, 'Salario': salario}
print(cadastro)
