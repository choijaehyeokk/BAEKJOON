# import sys
#
# N = int(sys.stdin.readline().rstrip()) #벽돌 개수
# shapes = []
# dp = [[0] * N for _ in range(N)]
# max_value = -1
# result = []
#
# for i in range(1, N+1):
#     area, h, w = map(int,sys.stdin.readline().split())
#     shapes.append((area, h, w, i))
#
# shapes.sort(key=lambda x : x[0], reverse=True)
# for i in range(N):
#     dp[i][i] = shapes[i][1]
#     current_blocks = [shapes[i]]
#     for j in range(i+1, N):
#         if shapes[j][2] < shapes[j-1][2]:
#             dp[i][j] = dp[i][j-1] + shapes[j][1]
#             current_blocks.append(shapes[j])
#         else:
#             flag = True
#             A = 0
#             for a in range(len(dp[i][:j])-1, -1, -1):
#                 if shapes[a][2] > shapes[j][2]:
#                     flag = False
#                     A = a
#                     break
#             if flag:
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i][a] + shapes[j][1]
#     if dp[i][-1] > max_value:
#         max_value = dp[i][-1]
#         result = current_blocks
#     #print(current_blocks)
# count = len(result)
# print(count)
# #print(result)
# for i in range(count):
#     print(result[count - i -1][3])

import sys
N = int(sys.stdin.readline().rstrip())
array = [(0,0,0,0)]
for i in range(1, N+1):
    a,h,w = map(int, sys.stdin.readline().split())
    array.append((i, a,h,w))

array.sort(key=lambda x : x[3])
dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(0,i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + array[i][2])
max_value = max(dp)
index = N
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index-=1
result.reverse()
print(len(result))
for i in result:
    print(i)
