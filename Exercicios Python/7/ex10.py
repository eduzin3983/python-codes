'''Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função de potência da
linguagem.'''

num1 = int(input())
num2 = int(input())

resultado = 0 

for i in range(0, num2+1):
    resultado += num1 * num1

print(resultado)