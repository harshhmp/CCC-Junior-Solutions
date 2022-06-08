num = int(input())
count = 0

for b in range(0, num//5 + 1):
    for a in range(0, num//4 + 1):
        if a * 4 + b * 5 == num:
            count += 1
        if a * 4 + b * 4 > num:
            break

if count == 0:
    print(0)
else:
    print(count)