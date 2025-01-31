'''Faça um programa que leia 5 números e informe o maior número'''
ler = [0, 0, 0, 0, 0]

for i in range(0, 5):
    ler[i] = float(input())

maior = max(ler)
print(f'O maior numero da lista {maior}')