#          CCC
#      J4 2018 Problem

N = input()
attr1 = []
for k in range(int(N)):
    attr1.append(input().split(" "))

if attr1[0][1] < attr1[0][0] and attr1[0][0] > attr1[1][0]:
    # 180 Degrees
    for i in range(0,len(attr1),1):
        attr1[i].reverse()
    attr1.reverse()

if attr1[0][1] < attr1[0][0] < attr1[1][0]:
    # 90 Degrees
    for i in range(len(attr1)):
        for j in range(i):
            attr1[i][j], attr1[j][i] = attr1[j][i], attr1[i][j]
    attr1.reverse()

if attr1[0][1] > attr1[0][0] > attr1[1][0]:
    # 260 Degrees
    attr1.reverse()
    for i in range(len(attr1)):
        for j in range(i):
            attr1[i][j], attr1[j][i] = attr1[j][i], attr1[i][j]


for h in attr1:
    Na = " ".join(h)
    print(Na)
