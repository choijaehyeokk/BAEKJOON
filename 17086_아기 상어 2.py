import sys, collections
N, M = map(int ,sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs():
    queue = collections.deque()
    queue.append([i, j, 0])
    visited[i][j]=1
    while queue:
        y, x, cnt = queue.popleft()
        if matrix[y][x]==1:
            return cnt
        for k in range(8):
            x_dist = x + dx[k]
            y_dist = y + dy[k]
            if x_dist < 0 or y_dist < 0 or x_dist >= M or y_dist >= N:
                continue
            if visited[y_dist][x_dist]:
                continue
            queue.append((y_dist, x_dist , cnt+1))
            visited[y_dist][x_dist] = 1
    return 0

max_dist = 0
for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        max_dist = max(bfs(), max_dist)
print(max_dist)


