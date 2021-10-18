First = input().split(" ")
Second = input().split(" ")
Third = input().split(" ")
Fourth = input().split(" ")

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count1V = 0
count2V = 0
count3V = 0
count4V = 0
count5 = 0


FirstV = [First[0], Second[0], Third[0], Fourth[0]]
SecondV = [First[1], Second[1], Third[1], Fourth[1]]
ThirdV = [First[2], Second[2], Third[2], Fourth[2]]
FourthV = [First[3], Second[3], Third[3], Fourth[3]]

for i in range(0, 4):
    count1 += int(First[i])
    count1V += int(FirstV[i])
for o in range(0, 4):
    count2 += int(Second[o])
    count2V += int(SecondV[o])
for p in range(0, 4):
    count3 += int(Third[p])
    count3V += int(ThirdV[p])
for q in range(0, 4):
    count4 += int(Fourth[q])
    count4V += int(FourthV[q])

Mylist = [count1, count2, count3, count4]
MylistV = [count1V, count2V, count3V, count4V]

for a in range(0, 4):
    if Mylist[0] == Mylist[a]:
        for b in range(0, 4):
            if Mylist[1] == Mylist[b]:
                for c in range(0, 4):
                    if Mylist[2] == Mylist[c]:
                        for d in range(0, 4):
                            if Mylist[3] == Mylist[d]:
                                continue
                            else:
                                count5 += 1
                                break
                    else:
                        count5 += 1
                        break
            else:
                count5 += 1
                break
    else:
        count5 += 1
        break

for e in range(0, 4):
    if MylistV[0] == MylistV[e]:
        for f in range(0, 4):
            if MylistV[1] == MylistV[f]:
                for g in range(0, 4):
                    if MylistV[2] == MylistV[g]:
                        for h in range(0, 4):
                            if MylistV[3] == MylistV[h]:
                                continue
                            else:
                                count5 += 1
                                break
                    else:
                        count5 += 1
                        break
            else:
                count5 += 1
                break
    else:
        count5 += 1
        break

if count5 > 0:
    print("not magic")
elif count5 == 0:
    print("magic")
