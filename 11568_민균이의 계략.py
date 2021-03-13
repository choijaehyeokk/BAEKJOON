import sys

N = int(sys.stdin.readline().rstrip())
dp = [1]
numbers = list(map(int,sys.stdin.readline().split()))

for i in range(1, N):
    dp.append(1)
    for j in range(i, -1, -1):
        if numbers[i] > numbers[j] :
            dp[i] = max(dp[i], dp[j] + 1)
dp = sorted(dp, reverse=True)
print(dp[0])