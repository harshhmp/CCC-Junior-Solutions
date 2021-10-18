#          CCC
#      J3 2018 Problem

# Gets Input and splits it into 4 different vars.
Inp = input()
NI = Inp.split(" ")
I1 = int(NI[0])
I2 = int(NI[1])
I3 = int(NI[2])
I4 = int(NI[3])

# Calculates all the inputs for output.
V0 = 0
V3 = I1
V13 = I1 + I2
V25 = I1 + I2 + I3
V30 = I1 + I2 + I3 + I4
V10 = I2
V22 = I2 + I3
V27 = I2 + I3 + I4
V12 = I3
V17 = I3 + I4
V5 = I4

# Prints out the 5 lines of output.
print(
    V0, V3, V13, V25, V30
)
print(
    V3, V0, V10, V22, V27
)
print(
    V13, V10, V0, V12, V17
)
print(
    V25, V22, V12, V0, V5
)
print(
    V30, V27, V17, V5, V0
)