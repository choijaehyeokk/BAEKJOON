# import sys, collections, heapq
# N = int(sys.stdin.readline().rstrip())
# problem_num = []
# #time = 1
# dead_cup = []
# result = 0
# result = []
# for i in range(1, N+1):
#     d, c = map(int,sys.stdin.readline().split())
#     dead_cup.append((d, c))
# dead_cup.sort(key=lambda x: x[0])
# queue = collections.deque(dead_cup)
# while queue:
#     if queue[0][0] == time:
#         #현재 deadline에 걸린 애들을 가지고 우선 최대를 뽑자.
#         current = queue.popleft()
#         cnt = current[1]
#         if not queue:
#             result += cnt
#             break
#         while queue[0][0] == time :
#             next = queue.popleft()
#             if cnt < next[1]:
#                 cnt = next[1]
#         result += cnt
#     else:
#         #deadline안걸리고 아직 여유로움, 그래서 다음 시간들 중에 하나 뽑아서 넣으면됨
#         while queue[0][0] < time:
#             queue.popleft()
#         if queue:
#             current = queue[0]
#             cnt = current[1]
#             for i in queue:
#                 if i[0] != current[0]: break
#                 if i[1] > cnt:
#                     current = i
#             result += current[1]
#             queue.remove(current)
#     time += 1
#
# print(result)

import sys, collections, heapq
N = int(sys.stdin.readline().rstrip())
dead_cup = []
result = []
for i in range(1, N+1):
    d, c = map(int,sys.stdin.readline().split())
    dead_cup.append((d, c))
dead_cup.sort(key=lambda x: x[0])


for i in dead_cup:
    dead = i[0]
    heapq.heappush(result, i[1])
    if dead < len(result):
        heapq.heappop(result)
print(sum(result))