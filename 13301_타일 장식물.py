import sys
N = int(sys.stdin.readline().rstrip())

def tiles(N: int):
    dp = [0]*(N+2)
    dp[1],dp[2] = 1, 1
    if N == 1: return 4
    elif N == 2: return 6

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return 2*(2*dp[N]+dp[N-1])

print(tiles(N))