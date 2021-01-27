import sys

calculation = list(sys.stdin.readline().split())


if int(calculation[0]) + int(calculation[2]) == int(calculation[4]):
    print("YES")
else:
    print("NO")