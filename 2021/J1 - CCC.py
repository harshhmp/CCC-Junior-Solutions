B = int(input())
SeaLevel = '0'
P = 5 * B - 400

if B > 100:
    SeaLevel = '-1'
if B < 100:
    SeaLevel = '1'
if B == 100:
    SeaLevel = '0'

print(P)
print(SeaLevel)