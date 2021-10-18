Num = int(input())
RollList = []
AScore = 100
DScore = 100
for i in range(Num):
    RollList.append(input().split(' '))

for set in RollList:
    if int(set[0]) > int(set[1]):
        DScore -= int(set[0])
    elif int(set[0]) < int(set[1]):
        AScore -= int(set[1])

print(AScore)
print(DScore)