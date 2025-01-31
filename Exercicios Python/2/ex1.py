''' Faça um Programa que peça dois números e imprima o maior deles. Se os dois números
forem iguais, imprima que são iguais. '''

x1 = int(input())
x2 = int(input())

if(x1 > x2):
    print(f'{x1} é maior que {x2}')
elif(x2 > x1):
    print(f'{x2} é maior que {x1}')
else:
    print('Sao Iguais')