import sys

string = sys.stdin.readline().rstrip()
one_two_cnt: int = 0
result: int = 0
for i in range(len(string)):
    if string[i] == '1' or string[i] == '2': one_two_cnt+=1

dp: list = [[0] * len(string) for _ in range(one_two_cnt+1)]

def encryption(dp: list, cnt: int):
    global result, string
    if int(string) < 1:
        return 0
    for i in range(1, cnt+1):
        for j in range(len(string)):
            if i == 1 and (string[j] == '1' or (string[j] == '2' and string[j+1] <= '6')): dp[i][j] = 1
            elif dp[i-1][j] >= 1:
                dp[i][j] = sum(dp[i-1][j+2:])
        result += sum(dp[i])

    return result+1

print(encryption(dp, one_two_cnt)%1000000)
#bugs exist