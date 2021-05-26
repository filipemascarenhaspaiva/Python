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


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.exercicio = True
        self.comida_thor = True
        self.humor = 100

    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome, "+("deve escolher entre fazer seus exercicios ou não" if self.exercicio else "você fez seus exercicios") + " e "+("esqueceu" if self.comida_thor else "lembrou")+" de alimentar seu cachorro."+"\nSeu humor esta em " + str(self.humor) + "% ."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.exercicio = True


if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    while True:
        print("-=-""-=-""-=-""-=-""-=-""-=-""-=-""-=-""-=-")
        print("São "+str(relogio)+" do dia "+str(dia) +
              ". Você tem que sair pro trabalho até às 08:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Tomar café da manhã")
        print("3 - Fazer exercicios ")
        print("4 - Dar comida para o cachorro")
        print("5 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            personagem.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == '2'):
            personagem.fome = False
            relogio.avancaTempo(30)
        elif(opcao == '3'):
            personagem.exercicio = False
            personagem.sujo
            relogio.avancaTempo(60)
        elif(opcao == '4'):
            personagem.comida_thor = False
            relogio.avancaTempo(10)
        elif(opcao == '5'):
            if personagem.fome == True:
                personagem.humor -= 10
            if personagem.sujo == True:
                personagem.humor -= 10
            if personagem.exercicio == True:
                personagem.humor -= 10
                personagem.sujo == True
            if personagem.comida_thor == True:
                personagem.humor -= 10
            if relogio.atrasado():
                personagem.humor -= 15
            print("-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("Você foi trabalhar.")
            print(personagem)
            print("-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
