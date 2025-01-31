'''Uma pessoa compra mensalmente 8 quilos de arroz e 5 quilos de feijão. Em um
dado mês, o preço do quilo de arroz e o do quilo de feijão eram, respectivamente,
R$ 2,20 e R$ 1,60. No mês seguinte, o preço do quilo de arroz teve um aumento de
10%, enquanto o quilo de feijão teve uma redução de 5%. Qual o aumento
percentual do gsto mensala dessa pessoa com a compra de arroz e feijão? '''


arroz = 8
feijao = 5

precoArroz = 2.20 
precoFeijao = 1.60

precoArroz2 = precoArroz * 1.1
precoFeijao2 = precoFeijao * 0.95


gastoInicial = (arroz * precoArroz) + (feijao * precoFeijao)

gastoFinal = (arroz * precoArroz2) + (feijao * precoFeijao2)

gastoTotal = gastoFinal - gastoInicial

percentual = (gastoTotal / gastoInicial) * 100             

print(f'{percentual:.02f}%')
