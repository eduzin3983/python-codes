produto = 1
estoque = 0
contador = 0

while produto != 0:
    produto = int(input())
    
    if(produto > 0):
        estoque += produto

    if(produto < 0):
        produto *= -1

        if(estoque > produto):
            estoque -= produto
            contador += 1
        else:
            print(f'Quantidade indisponível para a venda de {produto} unidades.')

print(f'Quantidade de vendas realizadas: {contador}')
print(f'Quantidade em estoque: {estoque}')