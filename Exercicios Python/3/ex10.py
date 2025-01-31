''' Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa nocrime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será
classificado como "Inocente". '''

p1 = input('Telefonou para a vítima?')
p2 = input('Esteve no local do crime?')
p3 = input('Mora perto da vítima?')
p4 = input('Devia para a vítima?')
p5 = input('Já trabalhou com a vítima?')

contador = 0
if(p1 == 'sim'):
    contador += 1
if(p2 == 'sim'):
    contador += 1
if(p3 == 'sim'):
    contador += 1
if(p4 == 'sim'):
    contador += 1
if(p5 == 'sim'):
    contador += 1

if(contador == 2):
    print('Suspeita')
elif(contador == 3 or contador == 4):
    print('Cúmplice')
elif(contador == 5):
    print('Assassino')
else:
    print('Inocente')
