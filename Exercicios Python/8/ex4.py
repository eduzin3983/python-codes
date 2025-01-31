'''Faça um programa que dada uma lista, o usuário pode procurar algum elemento
nesta lista. O programa deve dar uma das seguintes mensagens: Se o elemento
não for encontrado, “Elemento não está na lista”; Se for encontrado, “Elemento
encontrado na posição n da lista”.
Exemplo:
lista = [1,2,3,4,5]
Procurar: 6
Resultado: “Elemento não está na lista”
Procurar: 5
Resultado: “Elemento encontrado na posição 4 da lista.'''


n = int(input())
teste = False

lista = [1,3,5,8,4,2,7]
for i in range(len(lista)):
    if n == lista[i]:
        teste = True
        break

if teste == True:
    print(f'Elemento encontrado na posição {i+1} da lista.')
else:
    print('Elemento não está na lista')