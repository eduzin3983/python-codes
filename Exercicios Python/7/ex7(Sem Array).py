'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

soma = 0
for i in range(0, 5):
    ler = int(input())

    soma += ler

media = soma / 5

print(f'Soma: {soma}, Media {media}')