#          CCC
#      J2 2020 Problem

# Gets inputs
TP = int(input())  # Total Amount of people need to be infected
ND = int(input())  # Number of People infected on Day 0
Ra = int(input())  # The Rate of Infection

# Sets up Two counters for Output and Calculations
count = 0
count2 = 0

# Data Calculations
while True:
    count2 += ND
    ND *= Ra
    count += 1
    if count2 > TP:
        break
    else:
        continue

# Output
print(count - 1)
