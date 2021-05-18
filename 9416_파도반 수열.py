import sys
T = int(sys.stdin.readline().rstrip())

def P(n : int)->int:
    dp = [None, 1, 1, 1, 2, 2]
    if n <= 5:
        return dp[n]
    else:
        for i in range(6, n+1):
            dp.append(dp[i-1] + dp[i-5])
        #print(dp)
        return dp[n]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    result = P(N)
    print(result)