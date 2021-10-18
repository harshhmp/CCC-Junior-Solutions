#          CCC
#      J2 2018 Problem

# Gets Inputs
N = int(input())
Y = input()
T = input()


# Sets up the Counter For Output
count = 0

# Checks for 'C' in both arrays
for a in range(0, N):
    if Y[a] == 'C' and T[a] == 'C':
        count += 1

print(count)