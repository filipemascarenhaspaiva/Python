import random
print()
print('                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
print('                      ┃        Jogo da Vida        ┃                      ')
print('                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|')
print()
print('O objetivo é não zerar a sanidade ao longo de 5 dias, boa sorte!')
print()
nome = (input("Digite o Nome do seu Personagem? : "))


class Relogio_manha:
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


class Relogio_noite:
    def __init__(self):
        self.horas = 17
        self.minutos = 0

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 22 or (self.horas == 22 and self.minutos > 0))


class Acorda:
    def __init__(self):
        self.sujo = True
        self.fome = True


class Dormir:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.cansado = True
        self.sono = True


class Personagem_manha(Acorda):
    def __init__(self):
        super().__init__()
        self.exercicio = True
        self.comida_thor = True
        self.Pagar_conta_agua = True
        self.passar_roupa = True
        self.compras = True
        self.lavar_banheiro = True
        self.sanidade = 200

    def __str__(self):
        if dia == 1 or dia == 3 or dia == 5:
            return f"Ele está: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+", "+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Precisa fazer seus exercicios" if self.exercicio else f"\n⚫ {nome} fez seus exercicios")+("\n⚫ Esqueceu" if self.comida_thor else "\n⚫ Lembrou")+" de alimentar seu cachorro." + f"\n⚫ E sua sanidade esta em " + str(self.sanidade) + "% ."
        if dia == 2:
            return f"Ele está: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+", "+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Precisa pagar a conta de água" if self.Pagar_conta_agua else f"\n⚫ {nome} pagou a conta de água")+("\n⚫ Passar" if self.passar_roupa else "\n⚫ Já passou")+" suas roupas." + f"\n⚫ E sua sanidade esta em " + str(self.sanidade) + "% ."
        if dia == 4:
            return f"Ele está: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Precisa fazer compras" if self.compras else f"\n⚫ {nome} já fez suas compras")+("\n⚫ Lavar" if self.lavar_banheiro else "\n⚫ Já lavou")+" o banheiro" + f"\n⚫ E sua sanidade esta em " + str(self.sanidade) + "% "


class Personagem_noite(Dormir):
    def __init__(self):
        super().__init__()
        self.lavar_banheiro = True
        self.PassearCachorro = True
        self.Estudar = True
        self.LavarRoupa = True
        self.LigarFamilia = True
        self.VarrerAcasa = True
        self.ATv = True
        self.Escrever = True
        self.ComprarRoupa = True
        self.Cinema = True

    def __str__(self):
        if dia == 1:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu.")+("\n⚫ Precisando comprar roupas" if self.ComprarRoupa else "\n⚫ Renovou seu guarda-roupa")+("\n⚫ Devendo um passeio para o cachorro " if self.PassearCachorro else "\n⚫ Passeou com o cachorro ")+("\n⚫ Ver TV " if self.ATv else "\n⚫ Viu TV. ")+("\n⚫ E sua sanidade esta em " + str(personagem_manha.sanidade)) + "% "
        if dia == 2:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu.")+("\n⚫ Estudar" if self.Estudar else "\n⚫ Ja estudou")+("\n⚫ Lavar roupa" if self.LavarRoupa else "\n⚫ Roupas limpas")+("\n⚫ Ligar para a familia" if self.LigarFamilia else "\n⚫ Telefonou")+(f"\n⚫ E sua sanidade esta em " + str(personagem_manha.sanidade)) + "% "
        if dia == 3:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu.")+("\n⚫ Devendo um passeio para o cachorro " if self.PassearCachorro else "\n⚫ Passeou com o cachorro  ")+("\n⚫ Escrever no diário" if self.Escrever else "\n⚫ Descreveu seu dia")+("\n⚫ Ver TV " if self.ATv else "\n⚫ Viu TV ")+(f"\n⚫ E sua sanidade esta em " + str(personagem_manha.sanidade)) + "% "
        if dia == 4:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu.")+("\n⚫ Ir ao cinema" if self.Cinema else "\n⚫ O filme foi ótimo!!!!!")+("\n⚫ Varrer a casa" if self.VarrerAcasa else "\n⚫ Chão limpo")+("\n⚫ Estudar" if self.Estudar else "\n⚫ Ja estudou")+(f"\n⚫ E sua sanidade esta em " + str(personagem_manha.sanidade)) + "% "
        if dia == 5:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ Cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu.")+("\n⚫ Devendo um passeio para o cachorro " if self.PassearCachorro else "\n⚫ Passeou com o cachorro ")+("\n⚫ Ligar para a familia" if self.LigarFamilia else "\n⚫ Telefonou")+("\n⚫ Ver TV " if self.ATv else "\n⚫ Viu TV. ")+(f"\n⚫ E sua sanidade esta em " + str(personagem_manha.sanidade)) + "% "


if(__name__ == "__main__"):
    dia = 0
    relogio_manha = Relogio_manha()
    relogio_noite = Relogio_noite()
    personagem_manha = Personagem_manha()
    personagem_noite = Personagem_noite()

while personagem_manha.sanidade > 0:
    while True:
        dia += 1
        relogio_manha.horas = 6
        relogio_manha.minutos = 0
        while dia == 2:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio_manha)+" do Dia "+str(dia) +
                  f". {nome} tem que sair para o trabalho até às 08:00.")
            print(personagem_manha)
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
                if personagem_manha.Pagar_conta_agua == True:
                    print('Não tem água')
                    personagem_manha.sanidade -= 5
                elif personagem_manha.Pagar_conta_agua == False:
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

                    personagem_manha.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem_manha.sujo = True
                        relogio_manha.avancaTempo(15)
                        personagem_manha.sanidade -= 5
                    elif d4 != 1:
                        relogio_manha.avancaTempo(20)
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

                personagem_manha.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Sua omelete queimou e você ainda não saciou sua fome')
                    personagem_manha.fome = True
                    relogio_manha.avancaTempo(10)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_manha.avancaTempo(30)
            elif opcao == '3':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃               / ======= \                                            ┃')
                print(
                    '┃              / __________\           ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  ┃')
                print(
                    '┃             | ___________ |          ┃    Pagando conta de agua...┃  ┃')
                print(
                    '┃             | |   ENEL  | |          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  ┃')
                print(
                    '┃             | |         | |                                          ┃')
                print(
                    '┃             | |_________| |----.                                     ┃')
                print(
                    '┃             \=____________/     \                                    ┃')
                print(
                    '┃             / """"""""""" \      )                                   ┃')
                print(
                    '┃            / ::::::::::::: \   /T\                                   ┃')
                print(
                    '┃           (_________________)  \_/                                   ┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()
                ''
                personagem_manha.Pagar_conta_agua = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido a má conexão levou mais tempo do que o necessário')
                    relogio_manha.avancaTempo(30)
                    personagem_manha.sanidade -= 5
                if d4 != 1:
                    relogio_manha.avancaTempo(20)
            elif opcao == '4':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                           ┏━━━━━━━━━━━━━━━━━━━┓                      ┃')
                print(
                    '┃                           ┃  Passando Roupa...┃                      ┃')
                print(
                    '┃                           ┗━━━━━━━━━━━━━━━━━━━┛                      ┃')
                print(
                    '┃                                    ______                            ┃')
                print(
                    '┃            ______________        /| |/|\| |\                         ┃')
                print(
                    '┃          /    )\_ _/(    |      /_| ´ |.` |_\                        ┃')
                print(
                    '┃         ( --=(__/^\__)==-|        |   |.  |                          ┃')
                print(
                    '┃          \.______________|        |___|.__|                          ┃')
                print(
                    '┃             \. //.\ .//                                              ┃')
                print(
                    '┃══════════════════════════════════════════════════════════════════════┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()
                ''
                personagem_manha.passar_roupa = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Você se queimou com o ferro de passar')
                    relogio_manha.avancaTempo(5)
                    personagem_manha.passar_roupa = True
                    personagem_manha.sanidade -= 5
                if d4 != 1:
                    relogio_manha.avancaTempo(10)

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
                if personagem_manha.fome == True:
                    personagem_manha.sanidade -= 5
                if personagem_manha.sujo == True:
                    personagem_manha.sanidade -= 5
                if personagem_manha.Pagar_conta_agua == True:
                    personagem_manha.sanidade -= 5
                    personagem_manha.sujo == True
                if personagem_manha.passar_roupa == True:
                    personagem_manha.sanidade -= 5
                if relogio_manha.atrasado():
                    personagem_manha.sanidade -= 10
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi trabalhar no seguinte estado: ")
                print(personagem_manha)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem_manha.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem_manha.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                if personagem_manha.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        while dia == 4:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio_manha)+" do Dia "+str(dia) +
                  f". {nome} tem que sair pro trabalho até às 08:00.")
            print(personagem_manha)
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

                personagem_manha.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem_manha.sujo = True
                    relogio_manha.avancaTempo(15)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_manha.avancaTempo(20)
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

                if personagem_manha.compras == True:
                    print('Você precisa comprar seu café da manhã')
                    personagem_manha.sanidade -= 5
                if personagem_manha.compras == False:
                    personagem_manha.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'Sua omelete queimou e você ainda não saciou sua fome')
                        personagem_manha.fome = True
                        relogio_manha.avancaTempo(10)
                        personagem_manha.sanidade -= 5
                    elif d4 != 1:
                        relogio_manha.avancaTempo(30)

            elif opcao == '3':
                personagem_manha.compras = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido a má conexão você levou mais tempo do que o necessário')
                    relogio_manha.avancaTempo(40)
                if d4 != 1:
                    relogio_manha.avancaTempo(30)
            elif opcao == '4':
                personagem_manha.lavar_banheiro = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Você manchou sua roupa com candida')
                    personagem_manha.sanidade -= 5
                if d4 != 1:
                    relogio_manha.avancaTempo(10)
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
                if personagem_manha.fome == True:
                    personagem_manha.sanidade -= 5
                if personagem_manha.sujo == True:
                    personagem_manha.sanidade -= 5
                if personagem_manha.compras == True:
                    personagem_manha.sanidade -= 5
                    personagem_manha.sujo == True
                if personagem_manha.lavar_banheiro == True:
                    personagem_manha.sanidade -= 5
                if relogio_manha.atrasado():
                    personagem_manha.sanidade -= 10
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi trabalhar no seguinte estado: ")
                print(personagem_manha)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem_manha.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem_manha.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                if personagem_manha.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        while dia == 1 or dia == 3 or dia == 5:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio_manha)+" do Dia "+str(dia) +
                  f". {nome} tem que sair pro trabalho até às 08:00.")
            print(personagem_manha)
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

                personagem_manha.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem_manha.sujo = True
                    relogio_manha.avancaTempo(15)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_manha.avancaTempo(20)
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

                personagem_manha.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('Sua omelete queimou e você ainda não saciou sua fome')
                    personagem_manha.fome = True
                    relogio_manha.avancaTempo(10)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_manha.avancaTempo(30)
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

                personagem_manha.exercicio = False
                personagem_manha.sujo = True
                relogio_manha.avancaTempo(60)
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

                personagem_manha.comida_thor = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A comida do seu pet estava vencida e você teve que ir comprar ração nova')
                    relogio_manha.avancaTempo(20)
                if d4 != 1:
                    relogio_manha.avancaTempo(10)
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
                if personagem_manha.fome == True:
                    personagem_manha.sanidade -= 5
                if personagem_manha.sujo == True:
                    personagem_manha.sanidade -= 5
                if personagem_manha.exercicio == True:
                    personagem_manha.sanidade -= 5
                    personagem_manha.sujo == True
                if personagem_manha.comida_thor == True:
                    personagem_manha.sanidade -= 5
                if relogio_manha.atrasado():
                    personagem_manha.sanidade -= 10
                    print('Você chegou atrasado no trabalho')
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi trabalhar no seguinte estado: ")
                print(personagem_manha)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem_manha.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem_manha.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                if personagem_manha.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_manha.avancaTempo(5)
        personagem_manha.sujo = True
        personagem_manha.fome = True
        personagem_manha.exercicio = True
        personagem_manha.comida_thor = True

        # Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2
        # Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2
        # Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2
        # Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2#Estagio 2
        if personagem_manha.sanidade <= 0:
            print("Sua sanidade foi zerada, Você perdeu!")
            print()
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
            exit()
        print("-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
        print()
        print("Você chegou no trabalho, agora responda algumas perguntas para simular o seu desempenho profissional: ")
        print()
        print("-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
        print("Precione 0 para sair do jogo")

        class Questao:
            def __init__(self, Pergunta, Resposta,):
                self.Pergunta = Pergunta
                self.Resposta = Resposta

        Questoes_1 = [
            "\nCaminhando ao fim da tarde, uma senhora contou 20 casas em uma rua à sua direita. No regresso, ela contou 20 casas à sua esquerda. Quantas casas ela viu no total?\n(A) 20\n(B) 30\n(C) 10\n(D) 40\n\n",
            "\nA avó dividiu 20 balas entre as duas netas. Que horas são?\n(A) 10:02\n(B) 13:50\n(C) 20:02\n(D) 8:02\n\n",
            "\nEm que lugar vivem mais cangurus do que pessoas?\n(A) Indonésia\n(B) Nova Zelândia\n(C) Austrália\n(D) África do Sul\n\n",
            "\nQuanto mede uma girafa?\n(A) Entre 4,8 e 5,5 metros\n(B)  2 metros\n(C) Entre 5 e 6 metros\n(D) 4 metros\n\n",
        ]

        Questoes_2 = [
            "\nSe ontem fosse amanhã, hoje seria sexta-feira. Que dia é hoje?\n(A) segunda-feira\n(B) quarta-feira\n(C) sexta-feira\n(D) domingo\n\n",
            "\nQual a ciência que estuda a atmosfera da Terra e a climatologia?\n(A) Astronomia\n(B) Metereologia\n(C) Dispersão atmosférica\n(D) Climatologia\n\n",
            "\nQuantos braços tem um polvo?\n(A) Seis\n(B) Oito\n(C) Dez\n(D) Sete\n\n",
            "\n Qual das alternativas contém apenas animais cujos esqueletos são externos?\n(A) Caracóis, caranguejos e lagostas\n(B) Besouros, peixes e formigas\n(C) Caracóis, lulas e aranhas\n(D) Borboletas, caranguejos e peixes\n\n",
        ]

        Questoes_3 = [
            "\nQuantos planetas Terra cabem dentro do Sol?\n(A) Um milhão\n(B) Um bilhão\n(C) Cem\n(D) Cento e Cinquenta\n\n",
            "\nDe que são constituídos os diamantes?\n(A) Grafite\n(B) Carbono\n(C) Rênio\n(D) Ósmio\n\n",
            "\nQual dessas aves não voa?\n(A) Pinguim\n(B) Galinha\n(C) Cegonha\n(D) Peru\n\n",
            "\nO que é um Papiloscopista?\n(A) Especialista em cópias\n(B) Profissional especializado em identificação humana\n(C) Indivíduo responsável por crianças órfãs\n(D) Pessoa que tem uma pequena saliência cônica na língua\n\n",
        ]

        Questoes_4 = [
            "\nQual é respectivamente o animal terrestre mais lento e o personagem mais veloz?\n(A) Tartaruga e leão\n(B) Coala e cavalo\n(C) Caracol e tubarão\n(D) Bicho-preguiça e guepardo\n\n",
            "\nO que é Ortorexia?\n(A) Obsessão em falar de forma correta\n(B) Transtorno alimentar caracterizado pela perda de apetite\n(C) Obsessão pelo consumo de alimentos saudáveis\n(D) Preocupação exagerada em ter um corpo elegante\n\n",
            "\nQual desses autores brasileiros escreveu O Guarani e O Gaúcho?\n(A) Aluísio de Azevedo\n(B)  José de Anchieta\n(C) José de Alencar\n(D)  Gonçalves Dias\n\n",
            "\nO etanol é produzido através de qual fonte de energia?\n(A) Solar\n(B)  Biomassa\n(C) Eólica\n(D) Geotérmica\n\n",
            "\nQual destas, apesar do seu nome, não é considerada um tipo de força?\n(A) Força de atrito\n(B)  Força peso\n(C) Força centrípeta\n(D) Força eletromotriz\n\n",
        ]

        Questoes_5 = [
            "\nHomem Vitruviano é um desenho de qual artista famoso??\n(A) Michelangelo\n(B) Donatello\n(C) Van Gogh\n(D) Leonardo da Vinci\n\n",
            "\nPalavra “paz” soletrada através do alfabeto fonético da Otan:\n(A) Pá - amor - zuuum\n(B) Pisces - alfa - zelo\n(C) Paz - Aurélio - zulu\n(D) Papa - alfa - zulu\n\n",
            "\nO Dia do Fico é anualmente celebrado em que data?\n(A) 7 de setembro\n(B) 19 de abril\n(C) 19 de novembro\n(D) 9 de janeiro\n\n",
            "\nAs cantigas de Escárnio e Maldizer pertencem a qual escola literária?\n(A) Trovadorismo\n(B) Quinhentismo\n(C) Barroco\n(D) Classicismo\n\n",
            "\nO português é a língua oficial nesses três países:\n(A) Guiné-Bissau, África do Sul e Brasil\n(B) Guiné Equatorial, Cabo Verde e Angola\n(C) CegonVenezuela, Angola e Portugalha\n(D) Macau, Timor-Leste e Moçambique\n\n",
        ]

        Perguntas_1 = [
            Questao(Questoes_1[0], "a"),
            Questao(Questoes_1[1], "b"),
            Questao(Questoes_1[2], "c"),
            Questao(Questoes_1[3], "a"),
        ]
        Perguntas_2 = [
            Questao(Questoes_2[0], "b"),
            Questao(Questoes_2[1], "b"),
            Questao(Questoes_2[2], "a"),
            Questao(Questoes_2[3], "b"),
        ]
        Perguntas_3 = [
            Questao(Questoes_3[0], "a"),
            Questao(Questoes_3[1], "b"),
            Questao(Questoes_3[2], "a"),
            Questao(Questoes_3[3], "b"),
        ]
        Perguntas_4 = [
            Questao(Questoes_4[0], "d"),
            Questao(Questoes_4[1], "c"),
            Questao(Questoes_4[2], "c"),
            Questao(Questoes_4[3], "b"),
        ]
        Perguntas_5 = [
            Questao(Questoes_5[0], "d"),
            Questao(Questoes_5[1], "d"),
            Questao(Questoes_5[2], "d"),
            Questao(Questoes_5[3], "a"),
            Questao(Questoes_5[4], "b"),
        ]

        def Quiz_teste_1(Perguntas_1):
            acertos = 0
            erros = 0
            for Questao in Perguntas_1:
                Resposta = input(Questao.Pergunta).lower()
                if Resposta == '0':
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
                    exit()
                if Resposta == Questao.Resposta:
                    acertos += 1
                else:
                    erros += 1
                personagem_manha.sanidade = personagem_manha.sanidade - erros

            print("Voce acertou:", str(acertos) +
                  " Peguntas de:", str(len(Perguntas_1)))
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            if erros <= 2:
                print(
                    "Você teve um bom desempenho.")
            if erros >= 3:
                print(
                    "Seu desempenho foi péssimo. ")

        def Quiz_teste_2(Perguntas_2):
            acertos = 0
            erros = 0
            for Questao in Perguntas_2:
                Resposta = input(Questao.Pergunta).lower()
                if Resposta == '0':
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
                    exit()
                if Resposta == Questao.Resposta:
                    acertos += 1
                elif Resposta != Questao.Resposta:
                    erros += 1
                personagem_manha.sanidade = personagem_manha.sanidade - erros
            print("Voce acertou:", str(acertos) +
                  " Peguntas de:", str(len(Perguntas_2)))
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            if erros <= 2:
                print(
                    "Você teve um bom desempenho.")
            if erros >= 2:
                print(
                    "Seu desempenho foi péssimo.")

        def Quiz_teste_3(Perguntas_3):
            acertos = 0
            erros = 0
            for Questao in Perguntas_3:
                Resposta = input(Questao.Pergunta).lower()
                if Resposta == '0':
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
                    exit()
                if Resposta == Questao.Resposta:
                    acertos += 1
                elif Resposta != Questao.Resposta:
                    erros += 1
            personagem_manha.sanidade = personagem_manha.sanidade - erros
            print("Voce acertou:", str(acertos) +
                  " Peguntas de:", str(len(Perguntas_3)))
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            if erros <= 2:
                print(
                    "Você teve um bom desempenho.")
            if erros >= 3:
                print(
                    "Seu desempenho foi péssimo.")

        def Quiz_teste_4(Perguntas_4):
            acertos = 0
            erros = 0
            for Questao in Perguntas_4:
                Resposta = input(Questao.Pergunta).lower()
                if Resposta == '0':
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
                    exit()
                if Resposta == Questao.Resposta:
                    acertos += 1
                elif Resposta != Questao.Resposta:
                    erros += 1
                personagem_manha.sanidade = personagem_manha.sanidade - erros
            print("Voce acertou:", str(acertos) +
                  " Peguntas de:", str(len(Perguntas_4)))
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            if erros <= 2:
                print(
                    "Você teve um bom desempenho.")
            if erros >= 3:
                print(
                    "Seu desempenho foi péssimo.")

        def Quiz_teste_5(Perguntas_5):
            acertos = 0
            erros = 0
            for Questao in Perguntas_5:
                Resposta = input(Questao.Pergunta).lower()
                if Resposta == '0':
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
                if Resposta == Questao.Resposta:
                    acertos += 1
                elif Resposta != Questao.Resposta:
                    erros += 1
            personagem_manha.sanidade = personagem_manha.sanidade - erros
            print("Voce acertou:", str(acertos) +
                  " Peguntas de:", str(len(Perguntas_5)))
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            if erros <= 2:
                print(
                    "Você teve um bom desempenho.")
            if erros >= 3:
                print(
                    "Seu desempenho foi péssimo.")

        if dia == 1:
            Quiz_teste_1(Perguntas_1)
        if dia == 2:
            Quiz_teste_2(Perguntas_2)
        if dia == 3:
            Quiz_teste_3(Perguntas_3)
        if dia == 4:
            Quiz_teste_4(Perguntas_4)
        if dia == 5:
            Quiz_teste_5(Perguntas_5)
        if 0 < personagem_manha.sanidade < 50:
            print(f'{nome} terminou o segundo estagio do jogo com a sanidade em ',
                  personagem_manha.sanidade, '%, cuidado! você não pode zerar sua sanidade!')
        if 65 <= personagem_manha.sanidade < 80:
            print(f'{nome} terminou o segundo estagio do jogo com a sanidade em ',
                  personagem_manha.sanidade, '%')
        if personagem_manha.sanidade >= 80:
            print(f'{nome} terminou o segundo estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                  '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')

        # Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3
        # Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3
        # Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3
        # Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3
        # Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3#Estagio 3
        if personagem_manha.sanidade <= 0:
            print("Sua sanidade foi zerada, Você perdeu!")
            print()
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
            exit()
        print(
            "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
        print()
        print(f" Você saiu do trabalho e entrou carro: ")
        print()

        relogio_noite.horas = 17
        relogio_noite.minutos = 0
        while dia == 1:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio_noite)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem_noite)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Comprar roupas")
            print("4 - Levar o cachorro para passear")
            print("5 - Assistir TV")
            print("6 - Dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == '1':
                if personagem_noite.ComprarRoupa == False:
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

                    personagem_noite.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem_noite.sujo = True
                        relogio_noite.avancaTempo(15)
                        personagem_manha.sanidade -= 5
                    elif d4 != 1:
                        relogio_noite.avancaTempo(45)
                else:
                    print(
                        "Você precisa Comprar roupas no caminho de volta para casa.")
            elif opcao == '2':
                if personagem_noite.ComprarRoupa == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃         Jantando..         ┃                  ┃')
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

                    personagem_noite.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print('O arroz queimou e você ainda não saciou sua fome')
                        personagem_noite.fome = True
                        relogio_noite.avancaTempo(10)
                        personagem_manha.sanidade -= 5
                    elif d4 != 1:
                        relogio_noite.avancaTempo(45)
                else:
                    print(
                        "Você precisa Comprar roupas no caminho de volta para casa.")
            elif opcao == '3':
                personagem_noite.ComprarRoupa = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido ao transito você levou mais tempo do que o necessário')
                    relogio_noite.avancaTempo(135)
                if d4 != 1:
                    relogio_noite.avancaTempo(120)
            elif opcao == '4':
                if personagem_noite.ComprarRoupa == False:
                    personagem_noite.PassearCachorro = False
                    relogio_noite.avancaTempo(30)
                else:
                    print(
                        "Você precisa Comprar roupas no caminho de volta para casa.")
            elif opcao == '5':
                if personagem_noite.ComprarRoupa == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                                                                      ┃')
                    print(
                        '┃               __________             ┏━━━━━━━━━━━━━━━━━━━━┓          ┃')
                    print(
                        '┃             | ___________ |          ┃     Asistindo TV...┃          ┃')
                    print(
                        '┃             | |   Globo | |          ┗━━━━━━━━━━━━━━━━━━━━┛  	       ┃')
                    print(
                        '┃             | |         | |                                          ┃')
                    print(
                        '┃             | |_________| |                                          ┃')
                    print(
                        '┃       __    \=____________/               __                         ┃')
                    print(
                        '┃      / /                                  \ \                        ┃')
                    print(
                        '┃     / /____________________________________\ \                       ┃')
                    print(
                        '┃    (__________________________________________)                      ┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()
                    ''
                    personagem_noite.ATv = False
                    personagem_noite.cansado = False
                    relogio_noite.avancaTempo(60)
                else:
                    print(
                        "Você precisa Comprar roupas no caminho de volta para casa.")
            elif opcao == "6":
                if personagem_noite.ComprarRoupa == False:
                    personagem_noite.sono = False
                    if personagem_noite.fome == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.sujo == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.cansado == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.PassearCachorro == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.ComprarRoupa == True:
                        personagem_manha.sanidade -= 5
                    if relogio_noite.atrasado():
                        personagem_manha.sanidade -= 10
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    print(f"{nome} foi dormir no seguinte estado: ")
                    print(personagem_noite)
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    if 0 < personagem_manha.sanidade < 80:
                        print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                              '%, cuidado! você não pode zerar sua sanidade!')
                    if 80 <= personagem_manha.sanidade < 90:
                        print(
                            f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                    if personagem_manha.sanidade >= 90:
                        print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                              '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                    break
                else:
                    print(
                        "Você precisa Comprar roupas no caminho de volta para casa.")
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        while dia == 2:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            relogio_noite.avancaTempo(60)
            print("São "+str(relogio_noite)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem_noite)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Estudar")
            print("4 - Lavar roupa")
            print("5 - Ligar para a Familia ")
            print("6 - Dormir")
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

                personagem_noite.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem_noite.sujo = True
                    relogio_noite.avancaTempo(15)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '2':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃         Jantando..         ┃                  ┃')
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

                personagem_noite.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('O arroz queimou e você ainda não saciou sua fome')
                    personagem_noite.fome = True
                    relogio_noite.avancaTempo(10)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '3':
                personagem_noite.Estudar = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido a má conexão você levou mais tempo do que o necessário')
                    relogio_noite.avancaTempo(60)
                    personagem_manha.sanidade -= 5
                if d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '4':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃======!====!=====!=====!====!===!===!=====!===!===!===================┃')
                print(
                    '┃      /`\__/`\   /`\   /`\  |~| |~|  /)=I=(\  /`‘‘‘`\                 ┃')
                print(
                    '┃     |        | |   `"`   | | | | |  |  :  | |   :   |                ┃')
                print(
                    '┃     ‘-|    |-‘ ‘-|     |-‘ )/\ )/\  |  T  \ ‘-| : |-‘                ┃')
                print(
                    '┃       |    |     |     |  / \// \/  (  |\  |  ‘---‘                  ┃')
                print(
                    '┃       ‘.__.‘     ‘.___.‘  \_/ \_/   |  |/  /                         ┃')
                print(
                    '┃                                     |  /  /                          ┃')
                print(
                    '┃                                     |  \ /                           ┃')
                print(
                    '┃                                     ‘--‘`  ┏━━━━━━━━━━━━━━━━━━━┓     ┃')
                print(
                    '┃                                     ‘--‘`  ┃   Lavando Roupa...┃     ┃')
                print(
                    '┃                                            ┗━━━━━━━━━━━━━━━━━━━┛     ┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()
                personagem_noite.LavarRoupa = False
                relogio_noite.avancaTempo(45)

            elif opcao == '5':
                personagem_noite.LigarFamilia = False
                personagem_noite.cansado = False
                relogio_noite.avancaTempo(60)

            elif opcao == "6":
                personagem_noite.sono = True
                if personagem_noite.fome == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.sujo == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.cansado == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.Estudar == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.LavarRoupa == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.LigarFamilia == True:
                    personagem_manha.sanidade -= 5
                if relogio_noite.atrasado():
                    personagem_manha.sanidade -= 10
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi dormir no seguinte estado: ")
                print(personagem_noite)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem_manha.sanidade < 80:
                    print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem_manha.sanidade < 90:
                    print(
                        f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                if personagem_manha.sanidade >= 90:
                    print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        while dia == 3:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            relogio_noite.avancaTempo(60)
            print("São "+str(relogio_noite)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem_noite)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Levar o cachorro para passear")
            print("4 - Escrever no diário")
            print("5 - Ver TV")
            print("6 - Dormir")
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

                personagem_noite.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem_noite.sujo = True
                    relogio_noite.avancaTempo(15)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '2':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃         Jantando..         ┃                  ┃')
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

                personagem_noite.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('O arroz queimou e você ainda não saciou sua fome')
                    personagem_noite.fome = True
                    relogio_noite.avancaTempo(10)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '3':
                personagem_noite.PassearCachorro = False
                relogio_noite.avancaTempo(30)
            elif opcao == "4":
                personagem_noite.Escrever = False
                relogio_noite.avancaTempo(45)
            elif opcao == '5':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                                                                      ┃')
                print(
                    '┃               __________             ┏━━━━━━━━━━━━━━━━━━━━┓          ┃')
                print(
                    '┃             | ___________ |          ┃     Asistindo TV...┃          ┃')
                print(
                    '┃             | |   Globo | |          ┗━━━━━━━━━━━━━━━━━━━━┛  	       ┃')
                print(
                    '┃             | |         | |                                          ┃')
                print(
                    '┃             | |_________| |                                          ┃')
                print(
                    '┃       __    \=____________/               __                         ┃')
                print(
                    '┃      / /                                  \ \                        ┃')
                print(
                    '┃     / /____________________________________\ \                       ┃')
                print(
                    '┃    (__________________________________________)                      ┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()
                ''
                personagem_noite.ATv = False
                personagem_noite.cansado = False
                relogio_noite.avancaTempo(60)

            elif opcao == "6":
                personagem_noite.sono = True
                if personagem_noite.fome == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.sujo == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.cansado == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.PassearCachorro == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.Escrever == True:
                    personagem_manha.sanidade -= 5
                if relogio_noite.atrasado():
                    personagem_manha.sanidade -= 10
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi dormir no seguinte estado: ")
                print(personagem_noite)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem_manha.sanidade < 80:
                    print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem_manha.sanidade < 90:
                    print(
                        f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                if personagem_manha.sanidade >= 90:
                    print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        while dia == 4:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio_noite)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem_noite)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Ir ao cinema")
            print("4 - Varrer a casa")
            print("5 - Estudar")
            print("6 - Dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == '1':
                if personagem_noite.Cinema == False:
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

                    personagem_noite.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem_noite.sujo = True
                        relogio_noite.avancaTempo(15)
                        personagem_manha.sanidade -= 5
                    elif d4 != 1:
                        relogio_noite.avancaTempo(45)
                else:
                    print(
                        "Você precisa ir ao cinema no caminho de volta para casa.")
            elif opcao == '2':
                if personagem_noite.Cinema == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃         Jantando..         ┃                  ┃')
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

                    personagem_noite.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print('O arroz queimou e você ainda não saciou sua fome')
                        personagem_noite.fome = True
                        relogio_noite.avancaTempo(10)
                        personagem_manha.sanidade -= 5
                    elif d4 != 1:
                        relogio_noite.avancaTempo(45)
                else:
                    print(
                        "Você precisa ir ao cinema no caminho de volta para casa.")
            elif opcao == '3':
                personagem_noite.Cinema = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido ao transito você levou mais tempo do que o necessário')
                    relogio_noite.avancaTempo(135)
                if d4 != 1:
                    relogio_noite.avancaTempo(120)
                personagem_noite.cansado = False
            elif opcao == '4':
                if personagem_noite.Cinema == False:
                    personagem_noite.VarrerAcasa = False
                    relogio_noite.avancaTempo(30)
                else:
                    print(
                        "Você precisa ir ao cinema no caminho de volta para casa.")
            elif opcao == '5':
                if personagem_noite.Cinema == False:
                    personagem_noite.Estudar = False
                    relogio_noite.avancaTempo(60)
                else:
                    print(
                        "Você precisa ir ao cinema no caminho de volta para casa.")
            elif opcao == "6":
                if personagem_noite.Cinema == False:
                    personagem_noite.sono = False
                    if personagem_noite.fome == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.sujo == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.cansado == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.PassearCachorro == True:
                        personagem_manha.sanidade -= 5
                    if personagem_noite.ComprarRoupa == True:
                        personagem_manha.sanidade -= 5
                    if relogio_noite.atrasado():
                        personagem_manha.sanidade -= 10
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    print(f"{nome} foi dormir no seguinte estado: ")
                    print(personagem_noite)
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    if 0 < personagem_manha.sanidade < 80:
                        print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                              '%, cuidado! você não pode zerar sua sanidade!')
                    if 80 <= personagem_manha.sanidade < 90:
                        print(
                            f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade, '%')
                    if personagem_manha.sanidade >= 90:
                        print(f'{nome} terminou o terceiro estagio do jogo com a sanidade em ', personagem_manha.sanidade,
                              '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                    break
                else:
                    print(
                        "Você precisa ir ao cinema no caminho de volta para casa.")
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        while dia == 5:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            relogio_noite.avancaTempo(60)
            print("São "+str(relogio_noite)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem_noite)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Levar o cachorro para passear")
            print("4 - Ligar para familia")
            print("5 - Ver TV")
            print("6 - Dormir")
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

                personagem_noite.sujo = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                    personagem_noite.sujo = True
                    relogio_noite.avancaTempo(15)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '2':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃         Jantando..         ┃                  ┃')
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

                personagem_noite.fome = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print('O arroz queimou e você ainda não saciou sua fome')
                    personagem_noite.fome = True
                    relogio_noite.avancaTempo(10)
                    personagem_manha.sanidade -= 5
                elif d4 != 1:
                    relogio_noite.avancaTempo(45)
            elif opcao == '3':
                personagem_noite.PassearCachorro = False
                relogio_noite.avancaTempo(30)
            elif opcao == "4":
                personagem_noite.LigarFamilia = False
                relogio_noite.avancaTempo(45)
            elif opcao == '5':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                                                                      ┃')
                print(
                    '┃               __________             ┏━━━━━━━━━━━━━━━━━━━━┓          ┃')
                print(
                    '┃             | ___________ |          ┃     Asistindo TV...┃          ┃')
                print(
                    '┃             | |   Globo | |          ┗━━━━━━━━━━━━━━━━━━━━┛  	       ┃')
                print(
                    '┃             | |         | |                                          ┃')
                print(
                    '┃             | |_________| |                                          ┃')
                print(
                    '┃       __    \=____________/               __                         ┃')
                print(
                    '┃      / /                                  \ \                        ┃')
                print(
                    '┃     / /____________________________________\ \                       ┃')
                print(
                    '┃    (__________________________________________)                      ┃')
                print(
                    '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                print()
                ''
                personagem_noite.ATv = False
                personagem_noite.cansado = False
                relogio_noite.avancaTempo(60)

            elif opcao == "6":
                personagem_noite.sono = False
                if personagem_noite.fome == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.sujo == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.cansado == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.PassearCachorro == True:
                    personagem_manha.sanidade -= 5
                if personagem_noite.Escrever == True:
                    personagem_manha.sanidade -= 5
                if relogio_noite.atrasado():
                    personagem_manha.sanidade -= 10
                if personagem_manha.sanidade != 0:
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    print("Parabéns você venceu o jogo! ")
                    print()
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
                    exit()
            if(opcao == "0"):
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
                exit()
            else:
                print("Opção inválida!")
                relogio_noite.avancaTempo(5)
                continue
        personagem_noite.sujo = True
        personagem_noite.fome = True
        personagem_noite.cansado = True
        personagem_noite.sono = True
        personagem_noite.LigarFamilia = True
        personagem_noite.VarrerAcasa = True
        personagem_noite.ATv = True
        personagem_noite.Escrever = True
        personagem_noite.Estudar = True
if personagem_manha.sanidade <= 0:
    print("Sua sanidade foi zerada, Você perdeu!")
    print()
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
    exit()
