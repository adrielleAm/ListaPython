'''
1) Classe Retângulo: Crie uma classe que modele um retângulo:
a.	Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b.	Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c.	Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

'''


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, valor):
        self.__comprimento = valor

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, valor):
        self.__largura = valor

    def mudaValor(self):
        c = int(input("\nComprimento: "))
        self.comprimento = c

        l = int(input("Largura: "))
        self.largura = l

    def retornarValor(self):
        print("\nRetangulo")
        print("Comprimento: " + str(self.__comprimento) + " m")
        print("Largura: " + str(self.__largura) + " m")

    def calcArea(self):
        area = self.__comprimento * self.__largura
        print("A área é " + str(area) + " m²")

    def calcPerimetro(self):
        perimetro = (self.__comprimento * 2) + (self.__largura * 2)
        print("O perimetro é" + str(perimetro) + "m")


def main():

    c = int(input('Digite o comprimentro do local: '))
    l = int(input('Digite o largira do local: '))

    retangulo = Retangulo(c, l)

    retangulo.retornarValor()


main()
