'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões
que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o
estilo e o número de testes (divisões) executados.'''

n = int(input())

contador = 1
for i in range(1, n+1):
    resto = i % 2

    if(resto == 1):
        contador += 1
        print(i)

print(f'Numero de divisões: {contador}')
