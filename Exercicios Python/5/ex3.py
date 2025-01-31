'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.'''

paisA = 80000
paisB = 200000

anos = 0
while(paisA != paisB):
    anos += 1
    paisA *= 1.03
    paisB *= 1.015

print(anos)