'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago
por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da
prestação e o número de dias em atraso e passar estes valores para a função
valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que
a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o
programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja
informado um valor igual a zero para a prestação. Neste momento o programa deverá ser
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso,
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
juros por dia de atraso.'''

def valorPagamento(valor, diasAtraso):
    if dias > 0:
        valorFinal = (valor * 1.03) + (diasAtraso * 1.001)
    else:
        valorFinal = valor

    return valorFinal

n = 0
valorTotal = 0
while True:
    n += 0
    valor = int(input('valor: '))
    if valor == 0:
        print(f'quantidade: {n}')
        print(f'valor total de prestações: {valorTotal :.2f}')
        break
    else:
        dias = int(input('dias: '))
        print(f'{valorPagamento(valor, dias) :.2f}')
        valorTotal += valorPagamento(valor, dias)

