'''Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores
do cálculo de A! (A fatorial) e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120'''

num = int(input())

fatorial = 1
for i in range(num, 0, -1):
    fatorial = fatorial * i
    
print(fatorial)