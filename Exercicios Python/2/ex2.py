''' Faça um Programa que peça um valor diferente de zero e mostre na tela se o valor é
positivo ou negativo. Se o número digitado for zero, imprima “Número inválido”. '''

x = int(input())

if(x > 0):
    print('positivo')
elif(x < 0):
    print('negativo')
else:
    print('Numero invalido')