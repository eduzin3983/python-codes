''' Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo
grau e o programa não deve pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao
usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário; '''

a = float(input())
b = float(input())
c = float(input())

delta = b** - 4 * a * c


if(a == 0):
    print('a equação não é do segundo grau')
elif(delta < 0):
    print('a equação não possui raízes reais')
elif(delta == 0):
    x = (-b / 2 * a)
    print(f'a equação possui apenas uma raiz real que é: {x}')
else:
    x1 = (-b + (delta**1/2) / 2 * a)
    x2 = (-b - (delta**1/2) / 2 * a)

    print('a equação possui duas raízes reais')
    print(f'x1 = {x1}')
    print(f'x1 = {x2}')