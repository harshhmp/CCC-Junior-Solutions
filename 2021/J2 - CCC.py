Num = int(input())
BidList = []
PriceList = []

for i in range(Num):
    BidList.append([input(), input()])

for i in range(len(BidList)):
    PriceList.append(BidList[i][1])

PriceList.sort()
PriceList.reverse()

for i in range(len(BidList)):
    if BidList[i][1] == PriceList[0]:
        print(BidList[i][0])
        break