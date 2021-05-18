import sys

N = int(sys.stdin.readline().rstrip())

dp = [0,1,2]
if N >= 3:
    index = 0
    flag = -1
    while N-2 != index:
        if index % 3 == 0:
            dp[0] = (dp[1] + dp[2])% 15746
            flag = 0
        elif index % 3 == 1:
            dp[1] = (dp[0] + dp[2])% 15746
            flag = 1
        elif index % 3 == 2:
            dp[2] = (dp[0] + dp[1])% 15746
            flag = 2
        index += 1
    print(dp[flag])
else:
    print(dp[N] % 15746)
