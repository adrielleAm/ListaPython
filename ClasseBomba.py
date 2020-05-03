'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel
    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        alterarValor( ) – altera o valor do litro do combustível.
        alterarCombustivel( ) – altera o tipo do combustível.
        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
        OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''


class tipoCombustivel:
    tanque = {"GASOLINA": 100, "ALCOOL": 150}
    preco = {"GASOLINA": 4.00, "ALCOOL": 3.00}


class bombaCombustivel:

    def __init__(self, tipo_combustivel="G"):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = 0

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo):
        if tipo == "G":
            print("GASOLINA")
            self.__tipo_combustivel = "GASOLINA"
            self.valor_litro = tipoCombustivel.preco["GASOLINA"]

        elif tipo == "A":
            print("ALCOOL")
            self.__tipo_combustivel = "ALCOOL"
            self.valor_litro = tipoCombustivel.preco["ALCOOL"]

        else:
            print("O tipo selecionado não é válido")

    def alterar_combustivel(self):
        print("Digite G para Gasolina")
        print("Digite A para Alcool")
        tipo = input("Selecione o tipo desejado: ")
        self.tipo_combustivel = tipo

    def abastercer_valor(self):
        valor = float(input("\nAbastecer Valor: R$: "))
        litros = valor / self.valor_litro

        if bombaCombustivel.qtd_disponivel(self, litros):
            print("Abastecido " + str(litros) +
                  " litros de " + str(self.tipo_combustivel))
        else:
            print("Não há combustível dispónivel")

    def abastecer_litros(self):
        litros = float(input("\nAbastecer Litros: "))

        if bombaCombustivel.qtd_disponivel(self, litros):
            print(srt(litros) + " litros de " + self.tipo_combustivel +
                  "\nTotal R$ " + str((litros * self.valor_litro)))
        else:
            print("Não há combustível dispónivel")

    def alterar_valor(self):
        print("\nAlterar precos combustível")
        self.alterar_combustivel()

        novo_valor = float(input("Valor: R$ "))
        tipoCombustivel.preco[self.tipo_combustivel] = novo_valor

        print(self.tipo_combustivel + " valor alterado para R$ " +
              str(tipoCombustivel.preco[self.tipo_combustivel]))

    def alterar_qtd_combustivel():
        print("Gasolina: " +
              str(tipoCombustivel.tanque["GASOLINA"]) + " litros")
        print("Álcool: " + str(tipoCombustivel.tanque["ALCOOL"]) + " litros")

    def qtd_disponivel(self, litros):
        if litros <= tipoCombustivel.tanque[self.tipo_combustivel]:
            tipoCombustivel.tanque[self.tipo_combustivel] -= litros
            return True
        else:
            return False


def main():
    bomba = bombaCombustivel()
    while True:

        print("MENU BOMBA")
        print("1 - Escolher tipo combustível")
        print("2 - Abastecer por valor")
        print("3 - Abastecer por litros")
        print("4 - Alterar preços")
        print("5 - Preencher tanque das bombas")
        opcao = input("Selecionar:")

        if opcao == "1":
            bomba.alterar_combustivel()

        elif opcao == "2":
            bomba.abastercer_valor()

        elif opcao == "3":
            bomba.abastecer_litros()

        elif opcao == "4":
            bomba.alterar_valor()

        elif opcao == "5":
            bombaCombustivel.alterar_qtd_combustivel()
        else:
            print("Opção válida!")


main()
