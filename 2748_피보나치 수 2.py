import sys
N = int(sys.stdin.readline().rstrip())

def fibo(N: int)->int:
    dp: list = [0]*(N+2)
    dp[1],dp[2] = 1, 1

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

print(fibo(N))