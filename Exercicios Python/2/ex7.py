''' As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:
salários até R$ 280,00 (incluindo): aumento de 20%
salários entre R$ 280,00 e R$ 700,00: aumento de 15%
salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
• salário antes do reajuste;
• percentual de aumento aplicado;
• valor do aumento;
• novo salário, após o aumento '''

salario = float(input())

if(salario < 280):
    porcentagem = salario * 0.2
    r = salario + porcentagem
    

    print(f'Salario antes do reajuste {salario}')
    print(f'Aplicado 20%')
    print(f'Valor do aumento {porcentagem}')
    print(f'Novo Salario {r}')

elif(salario >= 280 and salario < 700):
    porcentagem = salario * 0.15
    r = salario + porcentagem
    

    print(f'Salario antes do reajuste {salario}')
    print(f'Aplicado 15%')
    print(f'Valor do aumento {porcentagem}')
    print(f'Novo Salario {r}')

elif(salario >= 700 and salario < 1500):
    porcentagem = salario * 0.1
    r = salario + porcentagem
    

    print(f'Salario antes do reajuste {salario}')
    print(f'Aplicado 10%')
    print(f'Valor do aumento {porcentagem}')
    print(f'Novo Salario {r}')

elif(salario >= 1500):
    porcentagem = salario * 0.05
    r = salario + porcentagem
    

    print(f'Salario antes do reajuste {salario}')
    print(f'Aplicado 5%')
    print(f'Valor do aumento {porcentagem}')
    print(f'Novo Salario {r}')