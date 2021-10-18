#          CCC
#      J1 2020 Problem

# Gets Inputs
S = int(input())
M = int(input())
L = int(input())

# Calculates the Happiness
TS = S * 1
TM = M * 2
TL = L * 3
TH = TS + TM + TL

# Looks if Total Happiness (TH) is over 10
if TH >= 10:
    print("happy")
else:
    print("sad")








