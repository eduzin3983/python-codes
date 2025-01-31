''' Faça um Programa que leia três números e mostre o maior e o menor deles. '''

x1 = int(input())
x2 = int(input())
x3 = int(input())

if(x1 > x2 and x1 > x3):
    print(f'Maior {x1}')
    if(x2 > x3):
        print(f'Menor {x3}')
    else:
        print(f'Menor {x2}')
    
elif(x2 > x3 and x2 > x1):
    print(f'Maior {x2}')
    if(x3 > x1):
        print(f'Menor {x1}')
    else:
        print(f'Menor {x3}')
elif(x3 > x1 and x3 > x2):
    print(f'Maior {x3}')

    if(x1 > x2):
        print(f'Menor {x2}')
    else:
        print(f'Menor {x1}')
else:
    print(f'Todos os numeros sao iguais: {x1}')