import sys, heapq

N, M = map(int, sys.stdin.readline().split())
problems = [i for i in range(1, N+1)]
priority = [[] for i in range(N+1)]
heap, result = [], []
heapq.heapify(heap)
degree = [0] * (N+1)
for _ in range(M):
    A, B = map(int ,sys.stdin.readline().split())
    priority[A].append(B)
    degree[B] += 1
for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)
while heap:
    value = heapq.heappop(heap)
    result.append(value)
    for y in priority[value]:
        degree[y] -= 1
        if degree[y] == 0:
            heapq.heappush(heap, y)
print(*result)