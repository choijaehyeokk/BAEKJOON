import sys
N = int(sys.stdin.readline().rstrip())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
B = sorted(list(map(int, sys.stdin.readline().split())))
S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)