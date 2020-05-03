'''
    Faça um Programa que leia um número e exiba o dia correspondente da semana. 
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

diaSemana = int(input('Número da semana: '))

if diaSemana == 1:
    print('1 - Domingo')
elif  diaSemana == 2:
    print('2 - Segunda')
elif  diaSemana == 3:
    print('3 - Terça')
elif  diaSemana == 4:
    print('4 - Quarta')
elif  diaSemana == 5:
    print('5 - Quinta')5
elif  diaSemana == 6:
    print('6 - Sexta')
elif  diaSemana == 7:
    print('7 - Sabado')
else:
    print('Valor Inválido')
