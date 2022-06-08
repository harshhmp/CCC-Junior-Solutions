import math
N = int(input())
positions = []
speeds = []
for i in range(N):

    positions.append(input().split(" "))
positions.sort()

for i in range(N-1):
    x = int(positions[i+1][1]) - int(positions[i][1])
    y = int(positions[i+1][0]) - int(positions[i][0])
    speeds.append(abs(x/y))

print(max(speeds))