import sys, collections

N, M = map(int, sys.stdin.readline().split())
queue = collections.deque([])
indgree = {}
result = []
graph = [[] for _ in range(N+1)]
print(graph)
for i in range(1, N+1):
    indgree[i] = 0

for _ in range(M):
    p1, p2 = map(int, sys.stdin.readline().split())
    indgree[p2] += 1
    graph[p1].append(p2)
    #p1이 p2보다 앞에 서야함.

#indgree가 0인 것부터 queue에 넣고 시작
for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    result.append(current)

    for i in graph[current]:
        indgree[i] -= 1
        if indgree[i] == 0:
            queue.append(i)
print(*result)