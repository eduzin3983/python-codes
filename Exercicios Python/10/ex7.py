'''Escreva um programa que pergunte ao usuário um número. Se o número for par,
calcule o valor desse número elevado ao cubo (n³), e se for ímpar, calcule o valor
quadro (n²). Seu programa deve perguntar quantos números ele o usuário quer
digitar. Ao final, seu programa deve apresentar a tabuada desse número.'''

def ler(qtdNumero):
    listaValor = []
    for i in range(qtdNumero):
        n = int(input())

        if n % 2 == 0:
            valor = n * n * n
        else:
            valor = n * n
        
        listaValor.append(valor)

    return listaValor

def tabuada(listaValor):
    for i in range(len(listaValor)):
        for j in range(1, 11):
            print(f'{listaValor[i]} * {j} == {listaValor[i] * j}')
        print('')


qtdNumero = int(input())

tabuada(ler(qtdNumero))





