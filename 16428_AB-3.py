import sys

A, B = map(int, sys.stdin.readline().split())
result : int = 0

if B < 0:
    print(int(A//abs(B)) * -1)
    print(int(A%abs(B)))
else:
    print(int(A//B))
    print(int(A%B))

