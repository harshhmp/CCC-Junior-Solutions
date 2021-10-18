import sys
text = input()
string = input()

cyclic = list(string)
ListStr = list(text)

for i in range(len(ListStr)):
    print(cyclic)
    print(i)
    print(ListStr[i])
    if ListStr[i] in cyclic:
        cyclic.remove(ListStr[i])
        if len(cyclic) == 0:
            print('yes')
            sys.exit()
    else:
        cyclic = list(string)
        if ListStr[i] in cyclic:
            cyclic.remove(ListStr[i])

print('no')