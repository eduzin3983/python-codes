'''desenvolver um algoritmo que efetue a soma de todos os números ímpares que são
múltiplos de três e que se encontram no conjunto dos números de 1 até 500.'''
soma = 0

for i in range(1, 501):
    teste1 = i % 2
    teste2 = i % 3
        
    if(teste1 == 1 and teste2 == 0):
        soma += i

print(soma)
