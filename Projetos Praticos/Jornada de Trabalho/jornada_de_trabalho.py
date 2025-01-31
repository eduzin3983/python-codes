v = int(input())
d = int(input())

horasExtras = 0
horasTrabalhadas = 0
tempoNormal = 0

for i in range(d):
    periodo = int(input())
    tempoTotal = 0

    for j in range(periodo):
        entrada = int(input())
        saida = int(input())
        tempoTotal += saida - entrada

    horasTrabalhadas += tempoTotal

    if tempoTotal > 8:
        horasExtras += tempoTotal - 8
        tempoNormal += 8
    else:
        tempoNormal += tempoTotal

if tempoNormal > 44:
    horasExtras += tempoNormal - 44
    tempoNormal = 44

valorDevido = (tempoNormal * v) + (horasExtras * (v * 1.5))

print(f'Horas trabalhadas: {horasTrabalhadas}')
print(f'Horas extras: {horasExtras}')
print(f'Valor devido: R$ {valorDevido:.2f}')