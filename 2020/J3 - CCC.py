# Inputs
from shlex import join

N = input()
LN = int(N) - 1
MLst = []
XLst = []
YLst = []
for i in range(int(N)):
    MLst.append(input().split(","))

for h in range(int(N)):
    XLst.append(int(MLst[h][0]))
    YLst.append(int(MLst[h][1]))
XLst.sort()
YLst.sort()

# Output
C1 = XLst[0] - 1  # Lowest X Number
C2 = XLst[LN] + 1  # Highest X Number
C3 = YLst[0] - 1  # Lowest Y Number
C4 = YLst[LN] + 1  # Highest Y Number

print(str(C1)+","+str(C3))
print(str(C2)+","+str(C4))
