import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int,sys.stdin.readline().split()))
dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True
result = []
for i in range(1, N+1):
    for j in range(M+1):
        if dp[i - 1][j] == False:
            continue
        if j - V[i-1] >= 0:
            dp[i][j - V[i-1]] = True
        if j + V[i -1] <= M:
            dp[i][j + V[i-1]] = True

for index, value in enumerate(dp[-1]):
    if value:
        result.append(index)
print(max(result) if result else -1)


