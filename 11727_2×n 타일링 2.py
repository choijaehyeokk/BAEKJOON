import sys

N = int(sys.stdin.readline().rstrip())
dp = [0, 1, 3]
for i in range(1, N-1):
    dp.append(dp[i] * 2 + dp[i+1])
print(dp[N] % 10007)