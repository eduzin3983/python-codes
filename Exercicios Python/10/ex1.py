'''Escreva uma função que retorne o maior de dois números.
Ex.:
Máximo (5,6) == 6
Máximo (2,1) == 2
Máximo (7,7) == 7'''
def maior(numero1, numero2):
    if(numero1 > numero2):
        maiorNumero = numero1
    else:
        maiorNumero = numero2
    
    return maiorNumero

n1 = int(input())
n2 = int(input())

print(f'Máximo ({n1},{n2}) == {maior(n1, n2)}')

