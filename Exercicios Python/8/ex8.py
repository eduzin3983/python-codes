'''Faça um Programa que leia 10 caracteres e armazene-os em uma lista. Ao final, diga
quantas consoantes foram lidas. Imprima as consoantes.'''

lista = []
vogais = []
consoantes = []
for i in range(10):
    lista.append(input())

for i in range(len(lista)):
    if lista[i] == 'a' or lista[i] == 'e' or lista[i] == 'i' or lista[i] == 'o' or lista[i] == 'u':
        vogais.append(lista[i])
    else:
        consoantes.append(lista[i])

print(consoantes)