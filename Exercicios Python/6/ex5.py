n = int(input("Informe o valor de n: "))
a, b = 1, 1

# Imprimir os dois primeiros valores da sequência
print(f'{a}, {b}, ', end='')

for _ in range(n-2):
    a, b = b, a + b
    print(f'{b}, ', end='')
