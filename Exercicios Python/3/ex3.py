''' Faça um programa que pergunte o preço de três produtos e informe qual produto você
deve comprar, sabendo que a decisão é sempre pelo mais barato. '''

p1 = float(input())
p2 = float(input())
p3 = float(input())

if(p1 < p2 and p1 < p3):
    print(f'Comprar produto 1')
elif(p2 < p1 and p2 < p3):
    print(f'Comprar produto 2')
else:
    print(f'Comprar produto 3')