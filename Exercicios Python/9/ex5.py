'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso.
Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973. '''

data = input()

dia = data[:2]
mes = int(data[3:5])
if mes == 1:
    mes = 'Janeiro'
elif mes == 2:
    mes = 'Fevereiro'
elif mes == 3:
    mes = 'Marco'
elif mes == 4:
    mes = 'Abril'
elif mes == 5:
    mes = 'Maio'
elif mes == 6:
    mes = 'Junho'
elif mes == 7:
    mes = 'Julho'
elif mes == 8:
    mes = 'Agosto'
elif mes == 9:
    mes = 'Setembro'
elif mes == 10:
    mes = 'Outubro'
elif mes == 11:
    mes = 'Novembro'
elif mes == 12:
    mes = 'Dezembro'
ano = data[6:10]
print(f'Você nasceu em {dia} de {mes} de {ano}.')