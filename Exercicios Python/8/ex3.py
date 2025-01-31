'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte
quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]; os valores lidos
devem ser armazenados de acordo com o seu valor. A entrada de dados deverá terminar quando
for lido um número negativo. Após o fim da leitura dos dados, informe quantos números foram
lidos em cada intervalor e exiba os números lidos.'''

intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []
while True:
    n = int(input())

    if n < 0:
        break
    elif n >= 0 and n <= 25:
        intervalo1.append(n)
    elif n > 25 and n <= 50:
        intervalo2.append(n)
    elif n > 50 and n <= 75:
        intervalo3.append(n)
    elif n > 75 and n <= 100:
        intervalo4.append(n)
    
print(f'Foram lidos {len(intervalo1)} numeros no intervalo de [0-25] sendo eles: {intervalo1}')
print(f'Foram lidos {len(intervalo2)} numeros no intervalo de [26-50] sendo eles: {intervalo2}')
print(f'Foram lidos {len(intervalo3)} numeros no intervalo de [51-75] sendo eles: {intervalo3}')
print(f'Foram lidos {len(intervalo4)} numeros no intervalo de [76-100] sendo eles: {intervalo4}')