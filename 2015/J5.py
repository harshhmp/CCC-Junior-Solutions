import sys

n = int(input())
k = int(input())
Flist = []
count = 0

if n == k or k == 1:
    print(1)
    sys.exit()

for i in range(k-1):
    Flist.append(1)
FirstNum = n-(k-1)
Flist.append(FirstNum)
count += 1
for a in range(k):
    print(Flist)
    Flist.clear()
    Flist.append(FirstNum - 1)