# import sys
# N, K = map(int, sys.stdin.readline().split())
# values : list = []
# current_value : int = 0
# max_weight: int = 0
# numbers: list = []
# for i in range(N):
#     W_V = list(map(int, sys.stdin.readline().split()))
#     numbers.append(W_V)
# numbers = sorted(numbers)
#
# for j in range(N):
#     for k in range(j, N):
#         max_weight += numbers[k][0]
#         if max_weight > K: max_weight = 0; break
#
#         current_value += numbers[k][1]
#         values.append(current_value)
#     current_value = 0
#
# print(max(values))
#

import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(1, k + 1):
        if j < w: dp[i][j] = dp[i - 1][j]
        else: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        print(dp)
print(dp[n][k])