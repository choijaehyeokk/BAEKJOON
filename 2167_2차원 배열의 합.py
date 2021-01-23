import sys
N, M = map(int, sys.stdin.readline().split())
matrix = []

for i in range(N):
    matrix.append(list(map(int,sys.stdin.readline().split())))
K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    i, j, x, y  = map(int, sys.stdin.readline().split())
    result: int = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            result += matrix[a][b]
    print(result)