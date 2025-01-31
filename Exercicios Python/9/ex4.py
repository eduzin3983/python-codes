'''Modifique o programa anterior de forma a mostrar o nome em formato de
escada.
F
FU
FUL
FULA
FULAN
FULANO'''

nome = input()

for i in range(len(nome)):
    for j in range(len(nome)):
        if j <= i:
            print(nome[j], end='')
    print('')