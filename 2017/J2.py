N = input()
NL = list(N)
K = int(input())
count = 0

for i in range(0,K+1):
    NL.append("0")
    KL = "".join(NL)
    count += int(KL)
    print(count)

C = list(str(count))
C.remove("0")
NC = "".join(C)
print(NC)