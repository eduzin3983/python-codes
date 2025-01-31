'''Altere o programa a seguir de forma que o usuário tenha 3 chances de acertar o
número. O programa termina se o usuário acerta ou erra 3 vezes. Faça o uso de
função.
import Random
n = random.randit(1,10)
x = int(input(“Escolha um número entre 1 e 10: ”))
if (x == n):
print(“Você acertou!”)
else:
print(“Você errou”)'''

import random

def acertar(n, x):
    if x == n:
        acertou = True
    else:
        acertou = False

    return acertou

n = random.randint(1, 10)
i = 1
while i <= 3:
    x = int(input('Escolha um número entre 1 e 10: '))
    if acertar(n, x) == True:
        print('Acertou!')
        break
    else:
        print(f'Errou! Tente de novo voce ainda tem {3 - i} tentaivas')
    i += 1
