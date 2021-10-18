Question = input()
N = input()
Dmo = input()
Peg = input()
Pairs = []

Lstdmo = Dmo.split(" ")
Lstpeg = Peg.split(" ")
for i in range(0, len(Lstdmo)):
    Lstdmo[i] = int(Lstdmo[i])
for i in range(0, len(Lstpeg)):
    Lstpeg[i] = int(Lstpeg[i])


def QuestionOne(Out):
    Lstdmo.sort()
    Lstpeg.sort()
    for i in range(int(N)):
        Temp = [int(Lstpeg[i]), int(Lstdmo[i])]
        if Temp[0] > Temp[1]:
            Out += Temp[0]
        elif Temp[0] < Temp[1]:
            Out += Temp[1]
        else:
            Out += Temp[0]
    print(Out)


def QuestionTwo(Out):
    Lstdmo.sort()
    Lstpeg.sort()
    Lst = []
    for speed in Lstpeg:
        Lst.append(speed)
    for speedk in Lstdmo:
        Lst.append(speedk)
    Lst.sort()
    Lst.reverse()
    for i in range(0, int(N)):
        Out += Lst[i]
    print(Out)


if Question == "1":
    QuestionOne(0)
elif Question == "2":
    QuestionTwo(0)
