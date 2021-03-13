import sys

def cal(stairs: list)->int:
    if len(stairs) == 1:
        return [0, stairs[0]]

    dp = [0]
    dp.append(stairs[0])#첫 번째 원소만 정해 놓음
    dp.append(stairs[1] + stairs[0])
    #print(stairs)
    for i in range(3, len(stairs)+1):
        dp.append(max(dp[i-3] + stairs[i-2] + stairs[i-1], dp[i-2] + stairs[i-1]))
    return dp

N = int(sys.stdin.readline().rstrip())
stairs = []

for _ in range(N):
    stairs.append(int(sys.stdin.readline().rstrip()))

result = cal(stairs)
print(result[N])