''''Escreva uma função que receba dois números e retorne True se o primeiro
número for múltiplo do segundo.
Ex.:
Múltiplo (8,4) == True
Múltiplo (7,3) == False
Múltiplo (5,5) == True'''

def multiplo(numero1, numero2):
    if(numero1 % numero2 == 0):
        multiplo = True
    else:
        multiplo = False
    
    return multiplo

n1 = int(input())
n2 = int(input())

print(f'Múltiplo ({n1},{n2}) == {multiplo(n1, n2)}')