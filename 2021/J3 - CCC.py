InputGo = True
CodeList = []
SplitCode = []
NumCodes = 0
PrivousDirection = ''

while InputGo:
    CodeList.append(input())
    NumCodes += 1
    if CodeList[NumCodes - 1] == '99999':
        break

NumCodes -= 1

for i in range(NumCodes):
    SplitCode.append(list(CodeList[i]))

for i in range(NumCodes):
    Sum = int(SplitCode[i][0]) + int(SplitCode[i][1])
    if Sum == 0:
        print(PrivousDirection + " " + SplitCode[i][2] + SplitCode[i][3] + SplitCode[i][4])
    elif (Sum % 2) == 0:
        PrivousDirection = 'right'
        print(PrivousDirection + " " + SplitCode[i][2] + SplitCode[i][3] + SplitCode[i][4])
    else:
        PrivousDirection = 'left'
        print(PrivousDirection + " " + SplitCode[i][2] + SplitCode[i][3] + SplitCode[i][4])