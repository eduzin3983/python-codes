dia = int(input('Dia da semana: '))
hora = int(input('Hora de início da sessão: '))
minuto = int(input('Minuto de início da sessão: '))
estudante = input('Estudante: ')
pagamento = input('Método de pagamento: ')

# converter hora
horaMinuto = hora + (minuto / 100) # 18:30 == 18.30

#Domingo
#Noturno
if(dia == 1 and horaMinuto >= 18.30): 
    preco = 30

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.3)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Vespertino
elif(dia == 1 and horaMinuto < 18.30): 
    preco = 30

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.3)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Segunda
#Noturno
if(dia == 2 and horaMinuto >= 18.30): 
    preco = 20

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco
    
#Vespertino
elif(dia == 2 and horaMinuto < 18.30): 
    preco = 15

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Terca
#Noturno
if(dia == 3 and horaMinuto >= 18.30): 
    preco = 20

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Vespertino
elif(dia == 3 and horaMinuto < 18.30): 
    preco = 15

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Quarta
#Noturno
if(dia == 4 and horaMinuto >= 18.30): 
    preco = 30

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Vespertino
elif(dia == 4 and horaMinuto < 18.30): 
    preco = 15

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Quinta
#Noturno
if(dia == 5 and horaMinuto >= 18.30): 
    preco = 30

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Vespertino
elif(dia == 5 and horaMinuto < 18.30): 
    preco = 20

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Sexta
#Noturno
if(dia == 6 and horaMinuto >= 18.30): 
    preco = 40

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.3)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Vespertino
elif(dia == 6 and horaMinuto < 18.30): 
    preco = 20

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Sabado
#Noturno
if(dia == 7 and horaMinuto >= 18.30): 
    preco = 40

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.2)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

#Vespertino
elif(dia == 7 and horaMinuto < 18.30): 
    preco = 30

    if(pagamento == 'C' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    elif(pagamento == 'C' and estudante == 'N'):
        ingresso = preco - (preco * 0.2)
    elif(pagamento == 'D' and estudante == 'S'):
        ingresso = preco - (preco * 0.5)
    else:
        ingresso = preco

print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))