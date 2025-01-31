'''O preço de venda de determinado produto é R$100,00 e tem a seguinte
composição: 60% referentes ao custo, 10% referentes ao lucro e 30% referentes
aos impostos. Em decorrência da crise econômica, houve um aumento de 10% no
custo desse produto. Porém, ao mesmo tempo, ocorreu uma redução de 20% no
valor dos impostos. Para aumentar as vendas do produto, o fabricante decidiu,
então, reduzir seu lucro à metade. Qual o valor atual de venda desse produto?'''


venda1 = 100
custo1 = 60
lucro1 = 10
impostos1 = 30

custo2 = custo1 * 1.1
impostos2 = impostos1 * 0.8
lucro2 = lucro1 / 2

r = custo2 + impostos2 + lucro2

print(r)