'''Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras
maiúsculas.
Dica: lembre−se que ao informar o nome, o usuário pode digitar letras maiúsculas
ou minúsculas.'''

nome = input()

for i in range(len(nome)-1, -1, -1):
    print(nome[i].upper(), end='')