'''
	Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''
def qtdNum(num1):
    print("O numero " + num1 + " é composto de " + str(len(num1)) + " digito(s)")
num1 = input('Digite um número: ')
qtdNum(num1)
