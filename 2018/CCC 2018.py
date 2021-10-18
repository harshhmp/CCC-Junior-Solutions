#          CCC
#      J1 2018 Problem

# List of Numbers To Ignore for First and Last Digits
my_list = (8, 9)

# Inputs for 4 Last Digits
Num1 = int(input())
Num2 = int(input())
Num3 = int(input())
Num4 = int(input())

# If Statements to see if number meets Criteria:
#   • the first of these four digits is an 8 or 9
#   • the last digit is an 8 or 9
#   • the second and third digits are the same
if Num1 in my_list:
    if Num2 == Num3:
        if Num4 in my_list:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")







