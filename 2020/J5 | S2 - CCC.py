column = int(input())
row = int(input())
rooms = []
run = True
tempfactors = []

for i in range(column):
    current_row = input().split(" ")
    rooms.append(current_row)


def print_factors(x):
    tempfactors.clear()
    for i in range(max(row, column)):
        if x % i == 0:
            tempfactors.append(i)

