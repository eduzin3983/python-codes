''' Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário
a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas
disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de
100, uma nota de 50, uma nota de5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. '''

saque = int(input('Valor do Saque: '))

if(saque >= 10 and saque <= 600):
    if(saque >= 100):
        notas100 = (saque // 100)
    else:
        notas100 = 0

    resultado = saque - (notas100 * 100)

    if(resultado >= 50 and resultado < 100):
        notas50 = 1
    else:
        notas50 = 0

    resultado = resultado - (notas50 * 50)

    if(resultado >= 10 and resultado < 50):
        notas10 = resultado // 10
    else:
        notas10 = 0
        
    resultado = resultado - (notas10 * 10)

    if(resultado >= 5 and resultado < 10):
        notas5 = 1
    else:
        notas5 = 0
        
    resultado = resultado - (notas5 * 5)

    if(resultado < 5 and resultado > 0):
        notas1 = resultado

    print(f'Para sacar a quantia de {saque} reais, precisara {notas100} nota(s) de 100, {notas50} nota(s) de 50, {notas10} uma nota(s) de 10, {notas5} uma nota(s) de 5 e {notas1} nota(s) de 1')

else:
    print('Maximo de saque é 600 reais')