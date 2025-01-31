d1 = int(input())
v1 = int(input())
t = int(input())
d2 = int(input())
v2 = int(input())

tempo_spacex = d1 / v1 
tempo_blueo = (d2 / v2) + (t * 24)

if tempo_spacex < tempo_blueo:
    print(True)
else:
    print(False)