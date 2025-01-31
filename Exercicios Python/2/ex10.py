''' Faça um programa que leia um caractere ‘F’ ou ‘C’, que indica se o próximo valor
corresponde à temperatura em Fahrenheit ou Celsius. Em seguida, o programa deve ler o
valor da temperatura e então imprimir o valor correspondente à temperatura na outra
unidade de medida. Observação: (C = 5/9 * (F - 32)) '''

medida = input()
temp = int(input())

if(medida == 'C'):
    c = 5/9 * (temp - 32)
    print(f'{temp} em graus celcius é {c}')
elif(medida == 'F'):
    f = (temp * 9/5) + 32
    print(f'{temp} em graus fahrenheit é {f}')
else:
    print('Valor Invalido')