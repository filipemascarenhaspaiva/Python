# Não consegui resolver por que o exercicio pede pra eu encapsular,
# ou seja, só permitir mexer nos atributos se chamar um método, mas
# é necessário colcoar condicionais com operadores relacionais ao
# alterar estes atributos pelo método. Não sei como resolver atendendo
# a todos os requisitos do exercicio


'''3. Crie uma classe Elevador para armazenar as informações de um 
elevador de prédio. A classe deve armazenar o andar atual 
(térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar
os seguintes métodos:

Inicializar: que deve receber como parâmetros a capacidade do 
elevador e o total de andares no prédio 
(os elevadores sempre começam no térreo e vazio);

Entrar: para acrescentar uma pessoa no elevador 
(só deve acrescentar se ainda houver espaço);

Sair: para remover uma pessoa do elevador 
(só deve remover se houver alguém dentro dele);

Subir: para subir um andar 
(não deve subir se já estiver no último andar);

Descer: para descer um andar 
(não deve descer se já estiver no térreo);

Obs.: Encapsular todos os atributos da classe (criar os métodos set e get)'''


class Elevador():
    def __init__(self):
        self.__andar = 0
        self.__andares = 0
        self.__pessoas = 0

    @property
    def andar(self):
        return self.__andar

    def puxa_andar(self):
        return self.__andar

    @andar.setter
    def andar(self, novo_andar):
        raise ValueError(
            ' Para alterar o andar você precisa ultilizar o método')

    def subir_andar(self, cima):
        return self.__andar == self.__andar + cima

    def descer_andar(self, baixo):
        return self.__andar == self.__andar + baixo

    @property
    def andares(self):
        return self.__andares

    def puxa_andares(self):
        return self.__andares

    @property
    def pessoas(self):
        return self.__pessoas

    def puxa_pessoas(self):
        return self.__pessoas

    @pessoas.setter
    def pessoas(self, novas_pessoas):
        raise ValueError(
            ' Para alterar as pessoas você precisa ultilizar o método')

    def acrecenta_pessoas(self, acrecentar):
        return self.__pessoas == self.__andar + acrecentar

    def diminui_pessoss(self, diminuir):
        return self.__pessoas == self.__andar - diminuir

    def inicializar(self, andar_inicial, andares_predio):
        Elevador.puxa_andar = andar_inicial
        Elevador.puxa_andares = andares_predio

    def entrar(self):
        Elevador.acrecenta_pessoas(self, 1)

    def sair(self):
        Elevador.diminui_pessoas(self, 1)

    def subir(self):
        Elevador.subir_andar(self, 1)

    def descer(self):
        Elevador.descer_andar(self, 1)


elevador = Elevador()

comeco = int(input('Em qual andar todo elevador tem que começar?: '))
print()
predio = int(input('Quantos andares tem esse predio?: '))
print()
elevador.inicializar(comeco, predio)
while comeco == 0:
    print('Opções: ')
    print()
    print('1. Acrecentar pessoa\n2. Remover pessoa\n3. Subir andar\n4. Descer andar\nOBS.. A capacidade máxima é de 5 pessoas')

    print()
    escolha = input('Escolha o que deseja realizar: ')

    if escolha == '1' and elevador.puxa_pessoas <= 5:
        elevador.entrar()
        print('temos agora ', elevador.puxa_pessoas, 'pessoas no elevador')
    elif escolha == '1' and elevador.puxa_pessoas > 5:
        print('Você atingiu a capácidade máxima, não é possível acrecentar mais pessoas')
    elif escolha == '2' and elevador.puxa_pessoas > 0:
        elevador.sair()
        print('temos agora ', elevador.puxa_pessoas, 'pessoas no elevador')
    elif escolha == '2' and elevador.puxa_pessoas <= 0:
        print('já não tem ninguem no elevador para você remover')
    elif escolha == '3' and elevador.puxa_andar < predio:
        elevador.subir()
        print('Estamos no ', elevador.puxa_andarm, 'º andar')
    elif escolha == '3' and elevador.puxa_andar >= predio:
        print('Você esta no ultimo andar, não é possível subir mais')
    elif escolha == '4' and elevador.puxa_andar > 0:
        elevador.descer()
    elif escolha == '4' and elevador.puxa_andar <= 0:
        print('Você esta no ultimo andar, não é possível descer mais')
    continue
print('Elevadores sempre começam no terreo=0')
