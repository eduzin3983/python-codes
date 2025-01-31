n = int(input())

for i in range(0, n):
    for j in range(i):
        print(f'{j+1} ', end='')
    print(i+1)