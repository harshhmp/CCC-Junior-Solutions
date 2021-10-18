inputYear = int(input())
answer = False
count = 0

while not answer:
    inputYear += 1
    listYear = list(str(inputYear))
    setYear = set(str(inputYear))
    duplicate = len(setYear) != len(listYear)
    if duplicate == False:
        answer = True
        
print(inputYear)
