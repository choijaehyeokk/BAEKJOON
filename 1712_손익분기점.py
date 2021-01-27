import sys

numbers = list(map(int, sys.stdin.readline().split()))

A = numbers[0]
B = numbers[1]
C = numbers[2]

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+ 1))
