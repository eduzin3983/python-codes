''''Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das
situações abaixo:
• É do sexo masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
• É do sexo masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
• É do sexo feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
• É do sexo feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição.
Crie um programa que leia um caractere (‘M’ ou ‘F’), que representa o sexo de um
indivíduo, e dois inteiros, que representam a idade e o tempo de contribuição. O programa
deverá então imprimir “Aposentável” se o indivíduo atenda uma das situações acima.
Caso contrário, o programa deverá imprimir “Não Aposentável” '''

sexo = input('Digite o seu sexo: ')
idade = int(input('Digite sua idade: '))
contribuicao = int(input('tempo de contribuição: '))

if(sexo == 'M' and idade >= 65 and contribuicao >= 10):
    print('Aposentável')
elif(sexo == 'M' and idade >= 63 and contribuicao >= 15):
    print('Aposentável')
elif(sexo == 'F' and idade >= 63 and contribuicao >= 10):
    print('Aposentável')
elif(sexo == 'F' and idade >= 61 and contribuicao >= 15):
    print('Aposentável')
else:
    print('Não Aposentável')