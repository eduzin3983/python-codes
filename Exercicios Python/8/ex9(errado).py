'''Faça um programa que leia duas sequências de números inteiros ordenados e imprima
uma sequência com os números ordenados das duas sequências anteriores. Você não deve
usar o método sort.
Exemplo:
Primeira sequência: 1 3 5 5 7 9 10
Segunda sequência: 2 2 4 6 8 8 10
Resultado: 1 2 2 3 4 5 5 6 7 8 8 9 10 10'''

lista1 = []
lista2 = []
listaSup = []
lista3 = []
#Lista 1
while True:
    n = int(input())

    if n < 0:
        break

    lista1.append(n)

#Lista 2
while True:
    n = int(input())

    if n < 0:
        break

    lista2.append(n)

# Testa qual lista é maior
maior = 0
if(len(lista1) > len(lista2)):
    maior = len(lista1)
else:
    maior = len(lista2)

# Junta as lista
for i in range(len(lista1)):
    listaSup.append(lista1[i])

for i in range(len(lista2)):
    listaSup.append(lista2[i])

# Ordena as listas
for i in range(len(listaSup)):
    for j in range(len(listaSup)):
        if(listaSup[j] < i):
            lista3.append(listaSup[j])

print(lista1)
print(lista2)
print(lista3)