'''
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota1 = int (input('Digite a nota do 1 bimestre: '))
nota2 = int (input('Digite a nota do 2 bimestre: '))
nota3 = int (input('Digite a nota do 3 bimestre: '))
nota4 = int (input('Digite a nota do 4 bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média das nota é: " + str(media))