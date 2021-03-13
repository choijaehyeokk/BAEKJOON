import sys

dp = [0,1,1]
N = int(sys.stdin.readline().rstrip())

for i in range(1, N-1):
    dp.append(dp[i] + dp[i+1])
print(dp[N])