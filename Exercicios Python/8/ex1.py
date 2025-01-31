'''Faça um programa que leia n notas, mostre as notas e a média.'''

n = int(input())

soma = 0
notas = []
for i in range(n):
    notas.append(int(input()))

    soma += notas[i]

media = soma / n

print(notas)
print(media)
