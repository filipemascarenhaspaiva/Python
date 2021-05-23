'''
Faça um programa que solicite um dado de nascimento (dd / mm / aaaa) e imprima com o nome do mês por extenso
exemplo de retorno.
entrada: 16/11/2015
saída: 16 de novembro de 2015
'''

meses = ["janeiro",
         "fevereiro",
         "março",
         "abril",
         "maio",
         "junho",
         "julho",
         "agosto",
         "setembro",
         "outubro",
         "novembro",
         "dezembro"]

dados = input("informe um dado (dd / mm / aaaa):")


print(dados . split("/")[0],
      "de",
      meses[(int(dados . split("/")[1]) - 1)],
      "de",
      dados . split("/")[2])
