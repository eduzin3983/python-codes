'''A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5,
-2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a
temperatura média.'''

T = [ -10, -8, 0, 1, 2, 5, -2, -4]

menor = 0
maior = 0
soma = 0
for i in range(len(T)):
    if T[i] < menor:
        menor = T[i]
    elif T[i] > maior:
        maior = T[i]

    soma += T[i]

media = soma / len(T)

print(menor)
print(maior)
print(media)