import sys

M = int(sys.stdin.readline().rstrip())
number : int = 1
for i in range(M):
    A, B = map(int,sys.stdin.readline().split())
    if A == number and B != number:
        number = B
    elif A != number and B == number:
        number = A
print(number)