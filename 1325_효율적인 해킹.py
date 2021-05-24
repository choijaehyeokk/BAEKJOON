# import sys, collections
#
# N, M = map(int,sys.stdin.readline().split())
# graph = [[] for _ in range(N+1)]
# can_hacking = {}
# result = []
# As = []
# def bfs(root):
#     if not(graph[root]):
#         return 0
#     queue = collections.deque([root])
#     visited = []
#     while queue:
#         current_node = queue.popleft()
#         if current_node not in visited:
#             visited.append(current_node)
#             if graph[current_node]:
#                 queue += list(set(graph[current_node]) - set(visited))
#     return len(visited)
#
# for _ in range(M):
#     A, B = map(int, sys.stdin.readline().split())
#     graph[B].append(A)
#     As.append(B)
#
# for a in set(As):
#     can_hacking[a] = 0
#     cnt = bfs(a)
#     can_hacking[a] = cnt
#
# max_value = max(can_hacking.values())
# for k, v in can_hacking.items():
#     if v == max_value:
#         result.append(k)
# print(*result)

import collections

n, m = map(int, input().split())
graph = [[] for _ in range(n +1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

def bfs(v):
    q = collections.deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in graph[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count+=1
    return count

result =  []
max_value = -1
for i in range(1, n +1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
print(*result)