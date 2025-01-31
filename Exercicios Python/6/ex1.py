'''Considere o seguinte menu:
    1 - Pizza de Marguerita
    2 - Pizza de Calabresa
    3 - Pizza de Pepperoni
    4 - Pizza de Mussarela
    5 - Sair
O seu programa deve: imprimir o menu; ler um número de 1 até 5; e imprimir a opção do
menu correspondente ao número lido. Isso deve ser repetido até que o usuário selecione
a opção 5'''
loop = True
while(loop == True):
    print('1 - Pizza de Marguerita')
    print('2 - Pizza de Calabresa')
    print('3 - Pizza de Pepperoni')
    print('4 - Pizza de Mussarela')
    print('5 - Sair')

    ler = int(input('Digite sua escolha: '))

    if(ler == 1):
        print('Pizza de Marguerita')
    elif(ler == 2):
        print('Pizza de Calabresa')
    elif(ler == 3):
        print('Pizza de Pepperoni')
    elif(ler == 4):
        print('Pizza de Mussarela')
    elif(ler == 5):
        loop = False
        print('Encerrando!')