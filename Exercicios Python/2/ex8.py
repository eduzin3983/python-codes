''' Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% '''

valorH = float(input('Valor das hora: '))
horasQ = float(input('Quantidade de hora: '))

resultadoVH = valorH * horasQ

if(resultadoVH <= 900):
    inss = resultadoVH * 0.1
    fgts = resultadoVH * 0.11

    salario = resultadoVH - inss

    print(f'Salario Bruto: ({valorH} * {horasQ}): {resultadoVH}')
    print(f'(-) IR (0%): 0')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total de Descontos: {inss}')
    print(f'Salario Liquido: {salario}')

elif(resultadoVH <= 1500):
    ir = resultadoVH * 0.5
    inss = resultadoVH * 0.1
    fgts = resultadoVH * 0.11

    salario = resultadoVH - ir - inss

    print(f'Salario Bruto: ({valorH} * {horasQ}): {resultadoVH}')
    print(f'(-) IR (5%): {ir}')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total de Descontos: {ir + inss}')
    print(f'Salario Liquido: {salario}')
    
elif(resultadoVH <= 2500):
    ir = resultadoVH * 0.1
    inss = resultadoVH * 0.1
    fgts = resultadoVH * 0.11

    salario = resultadoVH - ir - inss

    print(f'Salario Bruto: ({valorH} * {horasQ}): {resultadoVH}')
    print(f'(-) IR (10%): {ir}')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total de Descontos: {ir + inss}')
    print(f'Salario Liquido: {salario}')

else:
    ir = resultadoVH * 0.2
    inss = resultadoVH * 0.1
    fgts = resultadoVH * 0.11

    salario = resultadoVH - ir - inss

    print(f'Salario Bruto: ({valorH} * {horasQ}): {resultadoVH}')
    print(f'(-) IR (20%): {ir}')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total de Descontos: {ir + inss}')
    print(f'Salario Liquido: {salario}')