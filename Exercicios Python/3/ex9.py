''' Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica:
utilize o operador módulo (resto da divisão) '''

x1 = int(input())

res = x1 % 2

if(res == 0):
    print('Par')
else:
    print('Impar')