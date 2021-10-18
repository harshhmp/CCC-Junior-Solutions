# Input
N = input()
ILst = []
OLst = []
DLst = []
for i in range(int(N)):
    ILst.append(input().split(" "))

# Data Processing
for j in ILst:
    for a in range(int(j[0])):
        DLst.append(j[1])
    OLst.append(DLst)
    DLst = []

# Output
for h in OLst:
    Na = "".join(h)
    print(Na)