import sys

number = int(sys.stdin.readline().rstrip())

number %= 4
if number == 0 : print(2)
elif number == 2 : print(1)
else: print(0)
