Num = int(input())
Votes = input()
LVotes = list(Votes)
Acount = 0
Bcount = 0

for i in range(Num):
    if LVotes[i] == 'A':
        Acount += 1
    elif LVotes[i] == 'B':
        Bcount += 1

if Acount > Bcount:
    print('A')
elif Bcount > Acount:
    print('B')
else:
    print('Tie')