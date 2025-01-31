''''Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns
às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
Resultado: CTB
A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras
comuns a ambas. A ordem do resultado dependerá da lógica de programação utilizada. '''

str1 = input()
str2 = input()

resultado = []
for i in range(len(str1)):
    for j in range(len(str2)):
        if(str1[i] == str2[j]):
            resultado.append(str2[j])

for i in range(len(resultado)):
    print(resultado[i], end='')