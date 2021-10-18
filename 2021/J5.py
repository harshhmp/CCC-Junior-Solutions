Rows = int(input())
Col = int(input())
K = int(input())
Canvas = []
Row = []
inputList = []
counter = 0

for i in range(K):
    inputList.append(input().split(" "))

for n in range(Col):
    Row.append('B')
for i in range(Rows):
    Canvas.append(list(Row))

for i in range(K):
    if inputList[i][0] == 'R':
        for n in range(Col):
            R = int(inputList[i][1]) - 1
            if Canvas[R][n] == 'B': Canvas[R][n] = 'G'
            elif Canvas[R][n] == 'G': Canvas[R][n] = 'B'
    if inputList[i][0] == 'C':
        for n in range(Rows):
            C = int(inputList[i][1]) - 1
            if Canvas[n][C] == 'B': Canvas[n][C] = 'G'
            elif Canvas[n][C] == 'G': Canvas[n][C] = 'B'

for a in range(Rows):
    for b in range(Col):
        if Canvas[a][b] == 'G':
            counter += 1

print(counter)