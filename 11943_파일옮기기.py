import sys

A = list(map(int, list(sys.stdin.readline().split())))
B = list(map(int, list(sys.stdin.readline().split())))

print(min(A[0] + B[1], A[1] + B[0]))