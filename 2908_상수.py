import sys
A, B = map(int, sys.stdin.readline().split())
A, B = str(A)[::-1], str(B)[::-1]
print(A if int(A) > int(B) else B)