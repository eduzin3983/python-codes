''' Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''

x = int(input())

if(x == 1):
    print('Segunda')
elif(x == 2):
    print('Terca')
elif(x == 3):
    print('quarta')
elif(x == 4):
    print('quinta')
elif(x == 5):
    print('sexta')
elif(x == 6):
    print('sabado')
elif(x == 7):
    print('domingo')
else:
    print('Valor Invalido')