n = int(input())

for i in range(0, n):
    for j in range(i):
        print(' ', end='')
    print(i+1)