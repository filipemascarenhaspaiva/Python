class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 2

    def mudar_canal(self, novo_canal):
        if 2 <= novo_canal <= 50:
            self.canal = novo_canal
            print('Agora esta no canal ', self.canal)
        else:
            print('Canal Invalido')

    def mudar_volume(self, novo_volume):
        if 0 <= novo_volume <= 100:
            self.volume = novo_volume
            print('Agora esta no volume ', self.volume)
        else:
            print('Volume invalido')


televisao = TV()

print('Este televisor esta no canal 1 passando um jogo de futebol no volume 20')
print()
var_canal = int(
    input('Escolha um novo canal para colcoar na TV(Existem 100 canais): '))

televisao.mudar_canal(var_canal)

var_volume = int(input('Escolha um novo volume pra TV(Vai de 0 à 100): '))

televisao.mudar_volume(var_volume)
