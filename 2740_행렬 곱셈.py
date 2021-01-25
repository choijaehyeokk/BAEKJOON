import sys
A,B = [], []

N, M1 = map(int, sys.stdin.readline().split())
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
M2, K = map(int, sys.stdin.readline().split())
for _ in range(M2):
    B.append(list(map(int, sys.stdin.readline().split())))
cnt: int = 0
for a in range(N):
    for b in range(K):
        for c in range(M1):
            cnt += A[a][c] * B[c][b]
        print(cnt, end=' ')
        cnt = 0
    print()
