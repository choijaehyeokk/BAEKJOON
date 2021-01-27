import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
print(format(int(A, 2) * int(B, 2), 'b'))