import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

X : int = A*P
if P > C :
    Y = (P - C) * D + B
else:
    Y = B

print(X if X < Y else Y)

