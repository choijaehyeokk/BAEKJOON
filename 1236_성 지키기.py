import sys

N, M = map(int, sys.stdin.readline().split())
castle: list = []
col, row = [], []
for _ in range(N):
    castle.append(list(sys.stdin.readline().rstrip()))
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            col.append(i)
            row.append(j)
col_len, row_len= len(set(col)), len(set(row))
print(M - row_len if M - row_len > N - col_len else N - col_len)