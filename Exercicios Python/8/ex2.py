'''Altere o programa anterior de modo que o usuário possa inserir quantas notas ele desejar, sem
informa previamente esse número. Estabeleça algum critério de parada.'''

soma = 0
n = 0
notas = []
while True:
    nota = int(input())
    if(nota < 0):
        break

    notas.append(nota)
    
    soma += notas[n]
    n += 1

    
media = soma / n
print(notas)
print(media)
