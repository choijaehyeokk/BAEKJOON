import sys

N = int(sys.stdin.readline().rstrip())
dp = [0] * (N+1)
p = [0] * (N+1)
t = [0] * (N+1)
for i in range(1, N+1):
    T, P = map(int, sys.stdin.readline().split())
    if T + i <= (N+1):
        dp[i] = P
        p[i] = P
        t[i] = T

for j in range(2, N+1):
    for k in range(1, j):
        if j - k >= t[k]:
            dp[j] = max(dp[j], dp[k]+p[j])

print(max(dp))

