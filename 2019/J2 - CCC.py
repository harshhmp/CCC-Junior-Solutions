N = int(input())
P1 = input()
P2 = input()

P1L = list(P1)
P2L = list(P2)

a = []
b = []
count = 0

for i in range(0,N):
    P1I = P1L[i]
    if P1I == "C":
        a.append(i)
    else:
        continue

for o in range(0,N):
    P2I = P2L[o]
    if P2I == "C":
        b.append(o)
    else:
        continue

for p in a:
    for l in b:
        if p == l:
            count += 1
        else:
            continue
    else:
        continue

print(count)


