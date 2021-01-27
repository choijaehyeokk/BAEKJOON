import sys

number = int(sys.stdin.readline().rstrip())
result : int = 5
if number == 1: print(result)
else:
    for i in range(2, number+1):
        result += ((i+1)*3 - 2)
    print(result % 45678)