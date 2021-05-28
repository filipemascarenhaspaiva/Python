import random
print()

print('                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
print('                      ┃        Jogo da Vida        ┃                      ')
print('                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

nome = (input("Digite o Nome do seu Personagem? : "))


class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 8 or (self.horas == 8 and self.minutos > 0))


class Personagem135:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.exercicio = True
        self.comida_thor = True
        self.sanidade = 100

    def __str__(self):
        return f"Ele está: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+", "+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Precisa fazer seus exercicios" if self.exercicio else f"\n⚫ {nome} fez seus exercicios")+("\n⚫ Esqueceu" if self.comida_thor else "\n⚫ Lembrou")+" de alimentar seu cachorro." + f"\n⚫ E sua sanidade esta em " + str(self.sanidade) + "% ."


class Personagem2:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.Pagar_conta_agua = True
        self.passar_roupa = True
        self.sanidade = 100

    def __str__(self):
        return f"Ele está: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+", "+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Precisa pagar a conta de água" if self.Pagar_conta_agua else f"\n⚫ {nome} pagou a conta de água")+("\n⚫ Passar" if self.passar_roupa else "\n⚫ Já passou")+" suas roupas." + f"\n⚫ E sua sanidade esta em " + str(self.sanidade) + "% ."


class Personagem4:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.compras = True
        self.lavar_banheiro = True
        self.sanidade = 100

    def __str__(self):
        return f"Ele está: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+", "+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Precisa fazer compras" if self.compras else f"\n⚫ {nome} já fez suas compras")+("\n⚫ Lavar" if self.lavar_banheiro else "\n⚫ Já lavou")+" o banheiro." + f"\n⚫ E sua sanidade esta em " + str(self.sanidade) + "% ."


if(__name__ == "__main__"):
    dia = 0
    relogio = Relogio()
    personagem135 = Personagem135()
    personagem2 = Personagem2()
    personagem4 = Personagem4()
    while True:
        dia += 1
        relogio.horas = 6
        relogio.minutos = 0
        while dia == 2:
            personagem2.sanidade = personagem135.sanidade
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio)+" do Dia "+str(dia) +
                  f". {nome} tem que sair pro trabalho até às 08:00.")
            print(personagem2)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Tomar café da manhã")
            print("3 - Pagar a conta de água ")
            print("4 - Passar as roupas")
            print("5 - Ir trabalhar")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == '1':
                if personagem2.Pagar_conta_agua == True:
                    print('Não tem água')
                    personagem2.sanidade -= 5
                elif personagem2.Pagar_conta_agua == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
                    print(
                        '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃       _|___                _______  _______               _          ┃')
                    print(
                        '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
                    print(
                        '┃       || ||               |___o___||___o___|          ___| |         ┃')
                    print(
                        '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
                    print(
                        '┃       || ||                ||   ||  ||   ||           )__(           ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem2.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem2.sujo = True
                        relogio.avancaTempo(15)
                        personagem2.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(20)
            elif opcao == '2':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃    Tomando Café da manhã...┃                  ┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃                        ;)( ;                                         ┃')
                print(
                    '┃                       :----:     o8Oo./                              ┃')
                print(
                    '┃                      C|====| ._o8o8o8Oo_.                            ┃')
                print(
                    '┃                       |    |  \========/                             ┃')
                print(
                    '┃                       `----‘   ‘------‘                              ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                personagem2.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Sua omelete queimou e você ainda não saciou sua fome')
                    personagem2.fome = True
                    relogio.avancaTempo(10)
                    personagem2.sanidade -= 5
                elif d4 != 1:
                    relogio.avancaTempo(30)
            elif opcao == '3':
                personagem2.Pagar_conta_agua = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido ao transito você levou mais tempo do que o necessário')
                    relogio.avancaTempo(75)
                if d4 != 1:
                    relogio.avancaTempo(60)
            elif opcao == '4':
                personagem2.passar_roupa = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Você se queimou com o ferro de passar')
                    relogio.avancaTempo(5)
                    personagem2.passar_roupa = True
                    personagem2.sanidade -= 5
                if d4 != 1:
                    relogio.avancaTempo(10)

            elif opcao == '5':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
                print(
                    '┃                                                               ■■■■■■■┃')
                print(
                    '┃                           ____________                     ╔═════════┃')
                print(
                    '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
                print(
                    '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
                print(
                    '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
                print(
                    '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
                print(
                    '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
                print()
                if personagem2.fome == True:
                    personagem2.sanidade -= 10
                if personagem2.sujo == True:
                    personagem2.sanidade -= 10
                if personagem2.Pagar_conta_agua == True:
                    personagem2.sanidade -= 10
                    personagem2.sujo == True
                if personagem2.passar_roupa == True:
                    personagem2.sanidade -= 10
                if relogio.atrasado():
                    personagem2.sanidade -= 15
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi trabalhar no seguinte estado: ")
                print(personagem2)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem2.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem2.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem2.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem2.sanidade, '%')
                if personagem2.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem2.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
        while dia == 4:
            personagem4.sanidade = personagem135.sanidade
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio)+" do Dia "+str(dia) +
                  f". {nome} tem que sair pro trabalho até às 08:00.")
            print(personagem4)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Tomar café da manhã")
            print("3 - Fazer compras ")
            print("4 - Lavar o banheiro")
            print("5 - Ir trabalhar")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == '1':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
                print(
                    '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃       _|___                _______  _______               _          ┃')
                print(
                    '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
                print(
                    '┃       || ||               |___o___||___o___|          ___| |         ┃')
                print(
                    '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
                print(
                    '┃       || ||                ||   ||  ||   ||           )__(           ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                personagem4.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem4.sujo = True
                    relogio.avancaTempo(15)
                    personagem4.sanidade -= 5
                elif d4 != 1:
                    relogio.avancaTempo(20)
            elif opcao == '2':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃    Tomando Café da manhã...┃                  ┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃                        ;)( ;                                         ┃')
                print(
                    '┃                       :----:     o8Oo./                              ┃')
                print(
                    '┃                      C|====| ._o8o8o8Oo_.                            ┃')
                print(
                    '┃                       |    |  \========/                             ┃')
                print(
                    '┃                       `----‘   ‘------‘                              ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                if personagem4.compras == True:
                    print('Você precisa comprar seu café da manhã')
                    personagem4.sanidade -= 5
                if personagem4.compras == False:
                    personagem4.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print('Sua omelete queimou e você ainda não saciou sua fome')
                        personagem4.fome = True
                        relogio.avancaTempo(10)
                        personagem4.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(30)

            elif opcao == '3':
                personagem4.compras = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido ao transito você levou mais tempo do que o necessário')
                    relogio.avancaTempo(75)
                if d4 != 1:
                    relogio.avancaTempo(60)
            elif opcao == '4':
                personagem4.lavar_banheiro = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Você manchou sua roupa com candida')
                    personagem4.sanidade -= 10
                if d4 != 1:
                    relogio.avancaTempo(10)
            elif opcao == '5':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
                print(
                    '┃                                                               ■■■■■■■┃')
                print(
                    '┃                           ____________                     ╔═════════┃')
                print(
                    '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
                print(
                    '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
                print(
                    '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
                print(
                    '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
                print(
                    '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
                print()
                if personagem4.fome == True:
                    personagem4.sanidade -= 10
                if personagem4.sujo == True:
                    personagem4.sanidade -= 10
                if personagem4.compras == True:
                    personagem4.sanidade -= 10
                    personagem4.sujo == True
                if personagem4.lavar_banheiro == True:
                    personagem4.sanidade -= 10
                if relogio.atrasado():
                    personagem4.sanidade -= 15
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi trabalhar no seguinte estado: ")
                print(personagem4)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem4.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem4.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem4.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem4.sanidade, '%')
                if personagem4.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem4.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
        while dia == 1 or dia == 3 or dia == 5:
            if dia == 3:
                personagem135.sanidade = personagem2.sanidade
            if dia == 5:
                personagem135.sanidade = personagem4.sanidade
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio)+" do Dia "+str(dia) +
                  f". {nome} tem que sair pro trabalho até às 08:00.")
            print(personagem135)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Tomar café da manhã")
            print("3 - Fazer exercicios ")
            print("4 - Dar comida para o cachorro")
            print("5 - Ir trabalhar")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == "1":
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
                print(
                    '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃       _|___                _______  _______               _          ┃')
                print(
                    '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
                print(
                    '┃       || ||               |___o___||___o___|          ___| |         ┃')
                print(
                    '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
                print(
                    '┃       || ||                ||   ||  ||   ||           )__(           ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                personagem135.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem135.sujo = True
                    relogio.avancaTempo(15)
                    personagem135.sanidade -= 5
                elif d4 != 1:
                    relogio.avancaTempo(20)
            elif opcao == "2":
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃    Tomando Café da manhã...┃                  ┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃                        ;)( ;                                         ┃')
                print(
                    '┃                       :----:     o8Oo./                              ┃')
                print(
                    '┃                      C|====| ._o8o8o8Oo_.                            ┃')
                print(
                    '┃                       |    |  \========/                             ┃')
                print(
                    '┃                       `----‘   ‘------‘                              ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                personagem135.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Sua omelete queimou e você ainda não saciou sua fome')
                    personagem135.fome = True
                    relogio.avancaTempo(10)
                    personagem135.sanidade -= 5
                elif d4 != 1:
                    relogio.avancaTempo(30)
            elif opcao == "3":
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃       Fazendo exercicios...┃                  ┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃     █━━━━━█                                                          ┃')
                print(
                    '┃      \ ◙ /                                      _/█                  ┃')
                print(
                    '┃       \█/                                         ║                  ┃')
                print(
                    '┃       / \                                         ║                  ┃')
                print(
                    '┃      /   \           █━━━━━█           oo═════════oo                 ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                personagem135.exercicio = False
                personagem135.sujo = True
                relogio.avancaTempo(60)
            elif opcao == "4":
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃ Dando comida ao Cachorro...┃                   ┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                print(
                    '┃                                 __      _                            ┃')
                print(
                    '┃                               ○‘‘)}____//                            ┃')
                print(
                    '┃                                `_/      )                            ┃')
                print(
                    '┃           ║■■■■║   ║■■■■║       (_(_/-(_/                            ┃')
                print(
                    '┃                                                                      ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()

                personagem135.comida_thor = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A comida do seu pet estava vencida e você teve que ir comprar ração nova')
                    relogio.avancaTempo(20)
                if d4 != 1:
                    relogio.avancaTempo(10)
            elif(opcao == '5'):
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
                print(
                    '┃                                                               ■■■■■■■┃')
                print(
                    '┃                           ____________                     ╔═════════┃')
                print(
                    '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
                print(
                    '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
                print(
                    '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
                print(
                    '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
                print(
                    '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
                print()
                if personagem135.fome == True:
                    personagem135.sanidade -= 10
                if personagem135.sujo == True:
                    personagem135.sanidade -= 10
                if personagem135.exercicio == True:
                    personagem135.sanidade -= 10
                    personagem135.sujo == True
                if personagem135.comida_thor == True:
                    personagem135.sanidade -= 10
                if relogio.atrasado():
                    personagem135.sanidade -= 15
                    print('Você chegou atrasado no trabalho')
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi trabalhar no seguinte estado: ")
                print(personagem135)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem135.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem135.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem135.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem135.sanidade, '%')
                if personagem135.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem135.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            elif(opcao == "0"):
                print(
                    '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(
                    '                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
                print(
                    '                      ┃      Obrigado Por Jogar    ┃                      ')
                print(
                    '                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
                print(
                    '                                                                          ')
                break
            else:
                print("Opção inválida!")
                relogio.avancaTempo(5)
        if(opcao == "0"):
            break
        if dia == 5:
            print(
                '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print(
                '                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
            print(
                '                      ┃      Obrigado Por Jogar    ┃                      ')
            print(
                '                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
            print(
                '                                                                          ')
        personagem135.sujo = True
        personagem135.fome = True
        personagem135.exercicio = True
        personagem135.comida_thor = True
        continue
