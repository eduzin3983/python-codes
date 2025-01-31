''' Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece a
determinação a seguir:
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito
for D ou E. '''

nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))

resultado = (nota1 + nota2) / 2

if(resultado >= 9 and resultado <= 10):
    conceito = 'A'
    print(resultado)
    print(conceito)
    print('Aprovado')

elif(resultado >= 7.5 and resultado < 9):
    conceito = 'B'
    print(resultado)
    print(conceito)
    print('Aprovado')

elif(resultado >= 6 and resultado < 7.5):
    conceito = 'C'
    print(resultado)
    print(conceito)
    print('Aprovado')

elif(resultado >= 4 and resultado < 6):
    conceito = 'D'
    print(resultado)
    print(conceito)
    print('Reprovado')

elif(resultado < 4 and resultado > 0):
    conceito = 'E'
    print(resultado)
    print(conceito)
    print('Reprovado')

else:
    print('Nota Invalida')