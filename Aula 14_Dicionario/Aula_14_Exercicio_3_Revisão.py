import random
while True:
    inserido = input('Insira a senha para prossegui: ')
    senha = '12345678'
    if inserido != senha:
        print('Senha incorreta')
        continue
    else:
        break
print('Seja bem vindo!')
print()
print('Este é o jogo da advinhação, vou pensar em um numero entre 0 e 20 e você deve adivnhar: ')
print()
numero = random.randint(0, 20)
tentativas = 0
while True:
    chute = int(input('Digite o numero que eu estou pensando: '))
    if chute > numero:
        print('O numero que pensei é menor ')
        tentativas += 1
        continue
    elif chute < numero:
        print('O numero que pensei é maior ')
        tentativas += 1
        continue
    else:
        break
print(f'Parabens! Você acertou com apenas {tentativas} tentativas')
