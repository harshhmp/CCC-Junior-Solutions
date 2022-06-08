n = int(input())
villages = []

for i in range(n):
    villages.append(int(input()))
villages.sort()

m = max(villages) * 2

for i in range(1, n - 1):
    temp = (villages[i] - villages[i - 1]) / 2 + (villages[i + 1] - villages[i]) / 2
    if temp < m:
        m = temp

print(round(float(m), 1))
