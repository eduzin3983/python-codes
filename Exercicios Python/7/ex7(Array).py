'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''
ler = [0, 0, 0, 0, 0]
soma = 0

for i in range(0, 5):
    ler[i] = float(input())
    
    soma += ler[i]

media = soma / 5

print(f'Soma: {soma}, Media {media}')