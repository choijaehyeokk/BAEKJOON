import sys
N = int(sys.stdin.readline().rstrip())
dp = [0,1,2]
for i in range(3, N+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[N] % 10007)