'''Desenvolva um código em Python que gere um número aleatório de 
1 a 100 e dê ao usuário 10 chances para acertá-lo. A cada tentativa,
 deve ser impressa a quantidade de tentativas restantes e se o 
 número aleatório é maior ou menor do que o número inserido na 
 tentativa atual. Se o usuário não acertar em 10 tentativas, 
 informe qual o número aleatório. [Dica: use a função randint para 
 gerar o número aleatório]'''

import random
numero = random.randint(1, 100)


for adv in range(1, 11):
    adv = int(input('Tente acertar o numero sorteado de 1 a 100: '))
    if adv > numero:
        print(f'O numero sorteado é menor que {adv}')
    if adv < numero:
        print(f'O numero sorteado é maior que {adv}')
    if adv == numero:
        break
if adv == numero:
    print('Você acertou! Parabens!')

else:
    print(f'Suas tentativas terminaram, O numero sorteado era {numero}')
