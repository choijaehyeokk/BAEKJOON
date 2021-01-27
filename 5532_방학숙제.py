import sys

vac = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

for i in range(1, vac+1):
    A -= C
    B -= D
    if A <= 0 and B <= 0:
        print(vac - i)
        break