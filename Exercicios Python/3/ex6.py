''' Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
de centenas, dezenas e unidades do mesmo.
Observe os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
1, 7 e 16 '''

x1 = int(input())

if(x1 < 10):
    unidade = x1

    print(f'{x1} = {unidade} unidades')
elif(x1 < 100):
    unidade = x1 % 10
    dezena = x1 // 10

    print(f'{x1} = {dezena} dezena e {unidade} unidades')
elif(x1 < 1000):
    unidade = x1 % 10
    dezena = (x1 // 10) % 10
    centenas = x1 // 100

    print(f'{x1} = {centenas} centenas, {dezena} dezena e {unidade} unidades')
else:
    print("Numero Invalido")