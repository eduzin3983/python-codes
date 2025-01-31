'''Faça um programa que leia 5 números e informe o maior número'''

maior = int(input())

for i in range(2, 5):
    ler = int(input())

    if(ler > maior):
        maior = ler

print(maior)