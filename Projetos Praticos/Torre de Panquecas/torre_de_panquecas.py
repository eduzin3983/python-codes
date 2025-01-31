torre = [int(panqueca) for panqueca in input().split()]

m = []
while True:
    movimento = int(input())
    if movimento == 0:
        break
    m.append(movimento)

for i in m:
    torre[:i] = reversed(torre[:i])

if torre == sorted(torre):
    print("Torre estavel")
else:
    print("Torre instavel")