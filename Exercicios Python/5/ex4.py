'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas
de crescimentos iniciais. Valide a entrada e permita repetir a operação.'''

loop = True
while(loop == True):
    paisA = int(input('Digite quantos habitantes o pais A possui: '))
    taxaA = float(input('Digite a taxa de crescimento de A: '))

    paisB = int(input('Digite quantos habitantes o pais B possui: '))
    taxaB = float(input('Digite a taxa de crescimento de A: '))

    while(paisA < 0 or paisB < 0 or taxaA < 0 or taxaB < 0):
        paisA = int(input('Digite quantos habitantes o pais A possui: '))
        taxaA = float(input('Digite a taxa de crescimento de A: '))

        paisB = int(input('Digite quantos habitantes o pais B possui: '))
        taxaB = float(input('Digite a taxa de crescimento de A: '))

    taxaA = (taxaA / 100) + 1
    taxaB = (taxaB / 100) + 1

    anos = 0
    while(paisA != paisB):
        anos += 1
        paisA *= taxaA
        paisB *= taxaB

    print(f'O pais A e o pais B teram o mesmo numero de habtantes em {anos} anos')
    teste = input('Deseja repetir a operacao? S ou N: ')

    if(teste == 'S'):
        loop = True
    elif(teste == 'N'):
        loop = False
        print('Encerrando o programa!')
    else:
        loop = False
        print('caracter invalido, encerrando o programa')
