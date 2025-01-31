'''Escreva uma função que receba o lado (L) de um quadrado e retorne sua área
(A= lado²)
Ex.:
área_quadrado (4) == 16
área_quadrado (9) == 81'''

def area(lado):
    area = lado * lado
    return area

n = int(input())

print(f'área_quadrado ({n}) == {area(n)}')