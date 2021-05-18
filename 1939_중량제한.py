import sys, collections
N, M = map(int, sys.stdin.readline().split())
 = [[] for _ in range(N+1)]
start = 100000000
end = -1

def bfs(c, root, end):
    queue =collections.deque([root])
    visited = [False] * (N+1)
    visited[root] = True
    while queue:
        x = queue.popleft()
        for y, w in [x]:
            if not visited[y] and w >= c:
                visited[y] = True
                queue.append(y)
    return visited[end]

for _ in range(M):
    A,B,C = map(int, sys.stdin.readline().split())
    [A].append((B,C))
    [B].append((A,C))
    start = min(start, C)
    end = max(end, C)

start_node, end_node = map(int, sys.stdin.readline().split())
result = 0

while start <= end:
    mid = (start+end) // 2
    if bfs(mid, start_node, end_node):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
