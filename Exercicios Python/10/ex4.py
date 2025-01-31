'''Escreva uma função para validar uma variável string. Essa função recebe como
parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro
se o tamanho da string estiver entre os valores de máximo e mínimo, e falso, caso
contrário.'''

def validar(string):
    if(len(string) >= 0 and len(string) <= 10):
        validacao = True
    else:
        validacao = False

    return validacao

str = input()

print(f'{validar(str)}')