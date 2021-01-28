import sys
N, M = map(int, sys.stdin.readline().split())
A, B = [] , []

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    A.append(line)
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    B.append(line)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()