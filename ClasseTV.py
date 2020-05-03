'''
2) Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''


class tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, numero):
        num = numero
        if num >= 2 and num <= 65:
            self.__canal = num
        else:
            print("Canal Inválido")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numero):
        num = numero

        if num >= 0 and num <= 100:
            self.__volume = num
        else:
            print("O volume deve ser entre 0 e 100")

    def mudaCanal(self):
        num = int(input("CANAL: "))
        self.canal = num

    def mudaVolume(self):
        num = int(input("VOLUME: "))
        self.volume = num

    def __str__(self):
        return "CANAL:" + str(self.canal) + " \nVolume: " + str(self.volume)


def main():
    objTv = tv(2, 10)

    while True:
        print(objTv)

        print("MENU TV ---------")
        print("1 - mudar canal")
        print("2 - mudar volume")
        opcao = input("Selecionar:")

        if opcao == "1":
            objTv.mudaCanal()

        elif opcao == "2":
            objTv.mudaVolume()
        else:
            print("Opção válida!")


main()
