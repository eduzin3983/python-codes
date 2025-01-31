'''Faça um programa que leia um nome de usuário e a sua senha. Seu programa não
deve aceitar a senha igual ao nome do usuário; caso isso ocorra, mostre uma mensagem
de erro e volte a pedir as informações.'''

nome = input('Digite seu Nome: ')
senha = input('Digite uma senha diferente do seu nome: ')

while(nome == senha):
    print('Senha Invalida')

    nome = input('Digite seu Nome:  ')
    senha = input('Digite uma senha diferente do seu nome: ')