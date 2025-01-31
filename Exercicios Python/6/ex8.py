'''Escreva um algoritmo que imprima as seguintes sequências de números:
(1, 1 2 3 4 5 6 7 8 9 10)
(2, 1 2 3 4 5 6 7 8 9 10)
(3, 1 2 3 4 5 6 7 8 9 10)
(4, 1 2 3 4 5 6 7 8 9 10)'''


for i in range(1, 5):
    print(f'( {i}, ', end='')
    for j in range(1, 11):
        print(f'{j} ', end='')

        if(j == 10):
            print(')', end='')

    print()