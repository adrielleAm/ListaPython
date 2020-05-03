'''
	Faça um programa, com uma função que necessite de um argumento. 
    A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
    e ‘N’, se seu argumento for zero ou negativo.
'''
def tipoNum(num1):
    if(num1 > 0):
        print("P")
    else:
        print("N")
num1 = int (input('Digite um número: '))
tipoNum(num1)
