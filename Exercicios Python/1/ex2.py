'''Sob certas condições, o número de bactérias B de uma cultura, em função do
tempo t, medido em horas, é dado por B(t) = 2^(t/12). Qual será o número de
bactérias 6 dias após a hora zero?'''

dias = 6

t = dias * 24

B = 2**(t/12)

print(B)