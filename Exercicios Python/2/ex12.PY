''' Faça um programa que leia dois números e em seguida um caractere que representa
um operador aritmético (‘+’, ‘-’, ‘x’ ou ‘/’). Seu programa então deve imprimir o resultado
do operador aplicado aos dois números dados. '''

x1 = int(input('numero 1: '))
x2 = int(input('numero 2: '))

operacao = (input('+, -, x, /'))

if(operacao == '+'):
    print(x1 + x2)
elif(operacao == '-'):
    print(x1 - x2)
elif(operacao == 'x'):
    print(x1 * x2)
elif(operacao == '/'):
    print(x1 / x2)
else:
    print('Operacao Invalida')