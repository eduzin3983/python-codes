'''Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro
da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT'''

str1 = input()
str2 = input()

print(f'{str2} encontrado na posição {str1.find(str2)} de {str1}')