totalConstraints = 0
xNum = int(input())
xConstraints = []
xMatch = 0
yMatch = 0
temp = []
temp1 = 0
temp2 = 0
for i in range(xNum):
    temp = input().split(" ")
    xConstraints.append(temp)

yNum = int(input())
yConstraints = []
for i in range(yNum):
    temp = input().split(" ")
    yConstraints.append(temp)

gNum = int(input())
gGroups = []

for i in range(gNum):
    temp = input().split(" ")
    gGroups.append(temp)

for i in range(gNum):
    for j in range(xNum):
        temp1 = gGroups[i].count(xConstraints[j][0])
        temp2 = gGroups[i].count(xConstraints[j][1])
    if temp == 1 and temp2 == 1:
        xMatch += 1
    xMatch = xNum - xMatch
    totalConstraints = xMatch

for i in range(gNum):
    for j in range(yNum):
        temp1 = gGroups[i].count(yConstraints[j][0])
        temp2 = gGroups[i].count(yConstraints[j][1])
        if temp1 == 1 and temp2 == 1:
            yMatch += 1

totalConstraints += yMatch
print(totalConstraints)