''' Faça um Programa para leitura de três notas parciais de um aluno. O programa deve
calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10. '''

x1 = float(input('Nota 1: '))
x2 = float(input('Nota 2: '))
x3 = float(input('Nota 3: '))

media = (x1 + x2 + x3) / 3

if(media >= 7):
    print('Aprovado')

elif(media < 7):
    print('Reprovado')

elif (media == 10):
    print('Aprovado com distincao')