n = int(input())

heights = input().split(" ")
base = input().split(" ")

area = 0

for i in range(n):
    area += int(base[i]) * (int(heights[i]) + int(heights[i + 1])) / 2

print(area)