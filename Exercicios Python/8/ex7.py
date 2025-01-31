'''Faça um Programa que leia 10 números reais, armazene-os em uma lista e mostre-os
na ordem inversa ao final.'''

lista = []
for i in range(10):
    lista.append(int(input()))


print('[', end='')
for i in range(9, -1, -1):
    print(f'{lista[i]}', end='')
    print(', ', end='')
    
print(']')