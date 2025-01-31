'''Considerando-se um capital inicial (i) de R$10.000,00, aplicado a juros
compostos, durante 1 ano (n), à taxa de 2,5% ao mês (P), qual será o montante (M)
final? Considere a fórmula M = (P * (1 + (i * n)))^n para resolver este cálculo.'''

i = 10000
n = 12
p = 0.025

m = (p * (1 + (i * n)))**n

print(m)