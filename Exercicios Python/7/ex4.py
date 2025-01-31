'''Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.'''

for i in range(100, 201, 1):
    teste = i % 2

    if(teste == 1):
        print(i)