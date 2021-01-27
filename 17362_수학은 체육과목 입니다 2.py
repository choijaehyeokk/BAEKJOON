import sys

number = int(sys.stdin.readline().rstrip())

number %= 8
if number == 1 :
    print(1)
elif number == 0 or number == 2 :
    print(2)
elif number == 3 or number == 7 :
    print(3)
elif number == 4 or number == 6 :
    print(4)
elif number == 5 :
    print(5)